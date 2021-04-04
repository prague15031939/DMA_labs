using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Drawing;

namespace ChromosomesDetector
{
    public class ChromosomesDetector
    {
        private List<ImageObject> image;

        public ChromosomesDetector(List<ImageObject> image)
        {
            this.image = image;
        }

        public string Detect()
        {
            if (!isConsistentImage())
                return "invalid image";

            if (isBodyCentric())
                return "body centric chromosome";
            else if (isVShape())
                return "v shape chromosome";

            return "undefined chromosome";
        }

        private bool isConsistentImage()
        {
            image.Add(image[0]);
            try
            {
                for (int i = 0; i < image.Count - 1; i++)
                {
                    if (image[i].isVertical)
                    {
                        if (!(arePointsClose(image[i].upCenter, image[i + 1].downCenter) || arePointsClose(image[i].downCenter, image[i + 1].upCenter) ||
                            arePointsClose(image[i].upCenter, image[i + 1].rightCenter) || arePointsClose(image[i].upCenter, image[i + 1].leftCenter) ||
                            arePointsClose(image[i].downCenter, image[i + 1].rightCenter) || arePointsClose(image[i].downCenter, image[i + 1].leftCenter)))
                            return false;
                    }
                    else
                    {
                        if (!(arePointsClose(image[i].rightCenter, image[i + 1].leftCenter) || arePointsClose(image[i].leftCenter, image[i + 1].rightCenter) ||
                            arePointsClose(image[i].rightCenter, image[i + 1].downCenter) || arePointsClose(image[i].leftCenter, image[i + 1].downCenter) ||
                            arePointsClose(image[i].rightCenter, image[i + 1].upCenter) || arePointsClose(image[i].leftCenter, image[i + 1].upCenter)))
                            return false;
                    }
                }
                return true;
            }
            finally
            {
                image.RemoveAt(image.Count - 1);
            }
        }

        private bool isBodyCentric()
        {
            return isMatchStandard("abdbabcbabdbabcb");
        }

        private bool isVShape()
        {
            return isMatchStandard("ebabcbab");
        }

        private bool isMatchStandard(string standard)
        {
            for (int i = 0; i < standard.Length; i++)
            {
                if (getTerminalString() == standard)
                    return true;

                standard = standard.Substring(1) + standard[0];
            }

            return false;
        }

        private string getTerminalString()
        {
            StringBuilder sb = new StringBuilder();
            foreach (var item in image)
            {
                sb.Append(item.terminal.ToString());
            }
            return sb.ToString();
        }

        private bool arePointsClose(Point p1, Point p2)
        {
            return Math.Sqrt(Math.Pow(p1.X - p2.X, 2) + Math.Pow(p1.Y - p2.Y, 2)) <= 15;
        }
    }
}
