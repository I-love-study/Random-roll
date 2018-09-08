# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\ASUS_A84S\\Desktop\\bat\\python的学习之路\\随机点名\\随机点名.py'],
             pathex=['C:\\Users\\ASUS_A84S'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [('\\tupian\\huang.gif','C:\\Users\\ASUS_A84S\\Desktop\\bat\\python的学习之路\\随机点名\\tupian\\huang.gif','DATA')],
          [('\\tupian\\huaji.gif','C:\\Users\\ASUS_A84S\\Desktop\\bat\\python的学习之路\\随机点名\\tupian\\huaji.gif','DATA')],
          name='随机点名',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
