import sys
import os

from bs4 import BeautifulSoup
import markdown


class MarkdownToHtml:

    headTag = '<head><meta charset="utf-8" /></head>'

    def __init__(self,cssFilePath = None):
        if cssFilePath != None:
            self.genStyle(cssFilePath)

    def genStyle(self,cssFilePath):
        with open(cssFilePath,'r') as f:
            cssString = f.read()
        self.headTag = self.headTag[:-7] + '<style type="text/css">{}</style>'.format(cssString) + self.headTag[-7:]

    def markdownToHtml(self, sourceFilePath, destinationDirectory = None, outputFileName = None):
        if not destinationDirectory:
            # δ�������Ŀ¼��Դ�ļ�Ŀ¼(ע��Ҫת��Ϊ����·��)��Ϊ���Ŀ¼
            destinationDirectory = os.path.dirname(os.path.abspath(sourceFilePath))
        if not outputFileName:
            # δ��������ļ��������������ļ���
            outputFileName = os.path.splitext(os.path.basename(sourceFilePath))[0] + '.html'
        if destinationDirectory[-1] != '/':
            destinationDirectory += '/'
        with open(sourceFilePath,'r', encoding='utf8') as f:
            markdownText = f.read()
        # �����ԭʼ HTML �ı�
        rawHtml = self.headTag + markdown.markdown(markdownText,output_format='html5')
        # ��ʽ�� HTML �ı�Ϊ�ɶ��Ը�ǿ�ĸ�ʽ
        beautifyHtml = BeautifulSoup(rawHtml,'html5lib').prettify()
        with open(destinationDirectory + outputFileName, 'w', encoding='utf8') as f:
            f.write(beautifyHtml)


if __name__ == "__main__":
    mth = MarkdownToHtml()
    # ��һ�������в����б��ǳ�������������ű��ļ���
    argv = sys.argv[1:]
    # Ŀǰ�б� argv ���ܰ���Դ�ļ�·��֮���Ԫ�أ���ѡ����Ϣ��
    # �����������б� argv ���б��� markdown ʱ���б��е�Ԫ�ر���ȫ����Դ�ļ�·��
    outputDirectory = None
    if '-s' in argv:
        cssArgIndex = argv.index('-s') +1
        cssFilePath = argv[cssArgIndex]
        # �����ʽ���ļ�·���Ƿ���Ч
        if not os.path.isfile(cssFilePath):
            print('Invalid Path: '+cssFilePath)
            sys.exit()
        mth.genStyle(cssFilePath)
        # pop ˳��������仯
        argv.pop(cssArgIndex)
        argv.pop(cssArgIndex-1)
    if '-o' in argv:
        dirArgIndex = argv.index('-o') +1
        outputDirectory = argv[dirArgIndex]
        # ������Ŀ¼�Ƿ���Ч
        if not os.path.isdir(outputDirectory):
            print('Invalid Directory: ' + outputDirectory)
            sys.exit()
        # pop ˳��������仯
        argv.pop(dirArgIndex)
        argv.pop(dirArgIndex-1)
    # ���ˣ��б� argv �е�Ԫ�ؾ���Դ�ļ�·��
    # ��������Դ�ļ�·��
    for filePath in argv:
        # �ж��ļ�·���Ƿ���Ч
        if os.path.isfile(filePath):
            mth.markdownToHtml(filePath, outputDirectory)
        else:
            print('Invalid Path: ' + filePath)