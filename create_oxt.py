import zipfile, os, sys
import xml.etree.cElementTree as ET
import shutil
ProjectName = "TemplateRepo"

if __name__=="__main__":
    tree = ET.ElementTree(file=f"src\\description.xml")
    root = tree.getroot()
    versionAttr = root.findall(".//{http://openoffice.org/extensions/description/2006}version")[0].attrib
    version = versionAttr['value']
    extName = f"{ProjectName}-{version}(安裝時請刪除版號).oxt"
    orgName = f"{ProjectName}.oxt"
    zf = zipfile.ZipFile(extName, mode='w', compression = zipfile.ZIP_DEFLATED)
    os.chdir("src")
    for root, folders, files in os.walk(".\\"):
        for sfile in files:
            aFile = os.path.join(root, sfile)
            zf.write(aFile)
    zf.close()
    os.chdir("..")
    shutil.copy(f"{os.getcwd()}\\{extName}", f".\\{orgName}")