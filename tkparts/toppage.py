from tkparts.tkwindow import tkwindow 
import tkinter as tk
from tkinter import ttk

class toppage(tkwindow):
    def __init__(self, title):
        super().__init__(title)
        self.title = title
        self.tar_button = ttk.Button(text=u"tarファイルの解凍")
        self.tar_button.pack()
        self.log_merge = ttk.Button(text=u"logファイルのマージ")
        self.log_merge.pack()
        self.bk_search = ttk.Button(text=u"顧客操作ログの抽出")
        self.bk_search.pack()
        self.root.mainloop()


