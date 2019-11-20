using IronPython.Hosting;
using Microsoft.Scripting;
using Microsoft.Scripting.Hosting;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace IronPython调用示例
{
    class Program
    {
        static void Main(string[] args)
        {
            string logPath = Path.Combine("logs", "log.txt");
            if (File.Exists(logPath))
            {
                File.Delete(logPath);
            }
            FileStream fileStream = new FileStream(logPath, FileMode.OpenOrCreate);
            //Console.WriteLine("------------------------以下是C#执行日志信息------------------------");
            try
            {
                string pythonCodePath = Path.Combine("templates", "pythonCode.txt");
                string sourceCodePath = Path.Combine("pys", "performer.py");
                if (!File.Exists(pythonCodePath))
                {
                    throw new Exception("Python模板不存在！");
                }
                if (!File.Exists(sourceCodePath))
                {
                    throw new Exception("Python源代码文件不存在！");
                }
                string[] pythonCodeContent = File.ReadAllText(pythonCodePath).Split(new string[] { "\r\n" }, StringSplitOptions.None);
                string[] sourceCodeContent = File.ReadAllText(sourceCodePath).Split(new string[] { "\r\n" }, StringSplitOptions.None);
                if (sourceCodeContent == null || sourceCodeContent.Length == 0)
                {
                    throw new Exception("Python代码不能为空！");
                }
                List<string> strList = new List<string>(pythonCodeContent);
                foreach (var item in sourceCodeContent)
                {
                    strList.Add("        " + item);
                }
                string codes = "";
                foreach (var s in strList)
                {
                    codes += s + Environment.NewLine;
                }
                ScriptEngine engine = Python.CreateEngine();
                ScriptSource source = engine.CreateScriptSourceFromString(codes);
                ScriptScope scope = engine.CreateScope();
                source.Execute(scope);

                dynamic performer = scope.GetVariable("performer");
                dynamic per = performer("1005");
                per.run();
                var out_param = per.out_param;
                Console.WriteLine(per.out_param);
                Console.ReadKey();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);

                Console.ReadKey();
            }
            finally
            {
                fileStream.Close();
                fileStream.Dispose();
            }
        }
    }
}
