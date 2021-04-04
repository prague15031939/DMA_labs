using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ChromosomesDetector
{
    public enum Terminal
    {
        a, b, c, d, e, none
    }

    public partial class frmMain : Form
    {
        private Dictionary<Terminal, (int, int)> objectSizes = new Dictionary<Terminal, (int, int)>()
        {
            { Terminal.a, (40, 30) },
            { Terminal.b, (10, 90) },
            { Terminal.c, (30, 40) },
            { Terminal.d, (30, 50) },
            { Terminal.e, (110, 80) },
        };

        private Terminal pickedTerminal = Terminal.none;
        private List<ImageObject> image = new List<ImageObject>();

        private bool cursorMode = false;
        private ImageObject selectedItem = null;
        private bool outlines = true;
        private Point startPoint;

        public frmMain()
        {
            InitializeComponent();
            this.DoubleBuffered = true;
        }

        private void btnDetect_Click(object sender, EventArgs e)
        {
            MessageBox.Show(new ChromosomesDetector(image).Detect(), "chromosome type", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void cbTerminals_SelectedIndexChanged(object sender, EventArgs e)
        {
            pickedTerminal = (Terminal)cbTerminals.SelectedIndex;
        }

        private void pbImage_Paint(object sender, PaintEventArgs e)
        {
            Pen pen = new Pen(Color.Green, 2);

            foreach (var imageObject in image)
            {
                if (imageObject.terminal == Terminal.a && !imageObject.mirrored)
                    e.Graphics.DrawArc(pen, imageObject.coords.X, imageObject.coords.Y, imageObject.width, imageObject.height, 180.0F, 180.0F);
                if (imageObject.terminal == Terminal.a && imageObject.mirrored)
                    e.Graphics.DrawArc(pen, imageObject.coords.X, imageObject.coords.Y, imageObject.width, imageObject.height, 0.0F, 180.0F);
                else if (imageObject.terminal == Terminal.b)
                    e.Graphics.DrawLine(pen, imageObject.coords.X + imageObject.width / 2, imageObject.coords.Y, imageObject.coords.X + imageObject.width / 2, imageObject.coords.Y + imageObject.height);
                else if (imageObject.terminal == Terminal.c && !imageObject.mirrored)
                    e.Graphics.DrawArc(pen, imageObject.coords.X, imageObject.coords.Y, imageObject.width, imageObject.height, 0.0F, 180.0F);
                else if (imageObject.terminal == Terminal.c && imageObject.mirrored)
                    e.Graphics.DrawArc(pen, imageObject.coords.X, imageObject.coords.Y, imageObject.width, imageObject.height, 180.0F, 180.0F);
                else if (imageObject.terminal == Terminal.d && !imageObject.mirrored)
                    e.Graphics.DrawArc(pen, imageObject.coords.X, imageObject.coords.Y, imageObject.width, imageObject.height, 90.0F, 180.0F);
                else if (imageObject.terminal == Terminal.d && imageObject.mirrored)
                    e.Graphics.DrawArc(pen, imageObject.coords.X, imageObject.coords.Y, imageObject.width, imageObject.height, 90.0F, -180.0F);
                else if (imageObject.terminal == Terminal.e && !imageObject.mirrored)
                    e.Graphics.DrawArc(pen, imageObject.coords.X, imageObject.coords.Y, imageObject.width, imageObject.height, 0.0F, 180.0F);
                else if (imageObject.terminal == Terminal.e && imageObject.mirrored)
                    e.Graphics.DrawArc(pen, imageObject.coords.X, imageObject.coords.Y, imageObject.width, imageObject.height, 180.0F, 180.0F);

                if (outlines)
                    e.Graphics.DrawRectangle(new Pen(Color.Black, 1), imageObject.coords.X, imageObject.coords.Y, imageObject.width, imageObject.height);
            }
        }

        private void pbImage_Click(object sender, EventArgs e)
        {
            if (cursorMode || pickedTerminal == Terminal.none)
                return;

            var initialPoint = (e as MouseEventArgs).Location;

            var newImageObject = new ImageObject(initialPoint, pickedTerminal);
            newImageObject.SetSizes(objectSizes[pickedTerminal]);
            image.Add(newImageObject);

            pbImage.Invalidate();
        }

        private void cbTerminals_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Z)
                cursorMode = cursorMode ? false : true;
            else if (e.KeyCode == Keys.G)
                outlines = outlines ? false : true;

            if (e.KeyCode == Keys.M)
                image[image.Count - 1].Mirror();
            else if (e.KeyCode == Keys.Delete)
                image.RemoveAt(image.Count - 1);

            if (cursorMode || image.Count == 0)
            {
                pbImage.Invalidate();
                return;
            }

            var obj = image[image.Count - 1];
            if (e.KeyCode == Keys.Up)
                obj.coords = new Point(obj.coords.X, obj.coords.Y - 1);
            else if (e.KeyCode == Keys.Down)
                obj.coords = new Point(obj.coords.X, obj.coords.Y + 1);
            else if (e.KeyCode == Keys.Left)
                obj.coords = new Point(obj.coords.X - 1, obj.coords.Y);
            else if (e.KeyCode == Keys.Right)
                obj.coords = new Point(obj.coords.X + 1, obj.coords.Y);

            pbImage.Invalidate();
        }

        private void pbImage_MouseDown(object sender, MouseEventArgs e)
        {
            if (cursorMode)
            {
                var p = e.Location;
                foreach (var item in image)
                {
                    if (p.X >= item.coords.X && p.X <= item.coords.X + item.width &&
                        p.Y >= item.coords.Y && p.Y <= item.coords.Y + item.height)
                    {
                        selectedItem = item;
                        startPoint = e.Location;
                        break;
                    }
                }
            }
        }

        private void pbImage_MouseUp(object sender, MouseEventArgs e)
        {
            selectedItem = null;
        }

        private void pbImage_MouseMove(object sender, MouseEventArgs e)
        {
            if (cursorMode && selectedItem != null)
            {
                selectedItem.coords = new Point(selectedItem.coords.X + (e.X - startPoint.X), selectedItem.coords.Y + (e.Y - startPoint.Y));
                startPoint = e.Location;
                pbImage.Invalidate();
            }
        }
    }

    public class ImageObject
    {
        public Point coords { get; set; }
        public Terminal terminal { get; private set; }
        public int width { get; set; }
        public int height { get; set; }
        public bool mirrored { get; set; }
        public bool isVertical { get; private set; }

        public ImageObject(Point point, Terminal terminal)
        {
            this.coords = point;
            this.terminal = terminal;
            this.mirrored = false;
            this.isVertical = terminal == Terminal.b || terminal == Terminal.d ? true : false;
        }

        public void SetSizes((int, int) sizes)
        {
            width = sizes.Item1;
            height = sizes.Item2;
        }

        public void Mirror()
        {
            mirrored = mirrored ? false : true;
        }

        public Point leftCenter 
        {
            get
            {
                return new Point(coords.X, coords.Y + height / 2);
            }
        }
        public Point rightCenter
        {
            get
            {
                return new Point(coords.X + width, coords.Y + height / 2);
            }
        }

        public Point upCenter
        {
            get
            {
                return new Point(coords.X + width / 2, coords.Y);
            }
        }

        public Point downCenter
        {
            get
            {
                return new Point(coords.X + width / 2, coords.Y + height);
            }
        }
    }
}
