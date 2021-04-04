
namespace ChromosomesDetector
{
    partial class frmMain
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.pbImage = new System.Windows.Forms.PictureBox();
            this.cbTerminals = new System.Windows.Forms.ComboBox();
            this.btnDetect = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pbImage)).BeginInit();
            this.SuspendLayout();
            // 
            // pbImage
            // 
            this.pbImage.Location = new System.Drawing.Point(-4, 0);
            this.pbImage.Name = "pbImage";
            this.pbImage.Size = new System.Drawing.Size(898, 475);
            this.pbImage.TabIndex = 0;
            this.pbImage.TabStop = false;
            this.pbImage.Click += new System.EventHandler(this.pbImage_Click);
            this.pbImage.Paint += new System.Windows.Forms.PaintEventHandler(this.pbImage_Paint);
            this.pbImage.MouseDown += new System.Windows.Forms.MouseEventHandler(this.pbImage_MouseDown);
            this.pbImage.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pbImage_MouseMove);
            this.pbImage.MouseUp += new System.Windows.Forms.MouseEventHandler(this.pbImage_MouseUp);
            // 
            // cbTerminals
            // 
            this.cbTerminals.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cbTerminals.FormattingEnabled = true;
            this.cbTerminals.Items.AddRange(new object[] {
            "a (shoulder)",
            "b (side)",
            "c (hollow)",
            "d (side)",
            "e (base)"});
            this.cbTerminals.Location = new System.Drawing.Point(729, 24);
            this.cbTerminals.Name = "cbTerminals";
            this.cbTerminals.Size = new System.Drawing.Size(151, 28);
            this.cbTerminals.TabIndex = 1;
            this.cbTerminals.SelectedIndexChanged += new System.EventHandler(this.cbTerminals_SelectedIndexChanged);
            this.cbTerminals.KeyDown += new System.Windows.Forms.KeyEventHandler(this.cbTerminals_KeyDown);
            // 
            // btnDetect
            // 
            this.btnDetect.Location = new System.Drawing.Point(729, 67);
            this.btnDetect.Name = "btnDetect";
            this.btnDetect.Size = new System.Drawing.Size(151, 29);
            this.btnDetect.TabIndex = 2;
            this.btnDetect.Text = "analyze";
            this.btnDetect.UseVisualStyleBackColor = true;
            this.btnDetect.Click += new System.EventHandler(this.btnDetect_Click);
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(892, 476);
            this.Controls.Add(this.btnDetect);
            this.Controls.Add(this.cbTerminals);
            this.Controls.Add(this.pbImage);
            this.Name = "frmMain";
            this.Text = "ChromosomesDetector";
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.cbTerminals_KeyDown);
            ((System.ComponentModel.ISupportInitialize)(this.pbImage)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pbImage;
        private System.Windows.Forms.ComboBox cbTerminals;
        private System.Windows.Forms.Button btnDetect;
    }
}

