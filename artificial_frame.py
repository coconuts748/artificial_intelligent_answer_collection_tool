from na_mi_artificial_intelligent import na_mi_artificial_intelligent
from wen_xin_artificial_intelligent import wen_xin_artificial_intelligent
from dou_bao_artificial_intelligent import dou_bao_artificial_intelligent
from tkinter import ttk,messagebox
import tkinter
from loguru import logger
from data_part import data_part

class ArtificialFrame:
    def __init__(self,equal_root,set_title_name,set_geometry):
        self.equal_root = equal_root
        equal_root.title(f'{set_title_name}')

        if len(set_geometry) == 0:
            equal_root.geometry('300x300')
        elif len(set_geometry) != 0:
            equal_root.geometry(f'{set_geometry}')
        else:
            logger.info('set_geometry is null')

        self.na_mi_option = ttk.Button(equal_root,text='na_mi',command=self.na_mi_artificial_option)
        self.na_mi_option.pack()

        self.wen_xin_option = ttk.Button(equal_root,text='wen_xin',command=self.wen_xin_artificial_option)
        self.wen_xin_option.pack()

        self.dou_bao_option = ttk.Button(equal_root,text='dou_bao',command=self.dou_bao_artificial_option)
        self.dou_bao_option.pack()

    def na_mi_artificial_option(self):
        logger.info('na_mi_artificial_option running.......')
        if messagebox.askyesno('Tips','Be sure about your option?'):
            self.equal_root.destroy()
            def transmit_na_mi_search():
                logger.info('transmit_na_mi_search running ...')
                transmit_na_mi_input = str(transmit_na_mi.get().strip())
                if len(transmit_na_mi_input) == 0:
                    messagebox.showwarning('Error', 'invalid input')
                elif len(transmit_na_mi_input) != 0:
                    if messagebox.askyesno('Tips', 'whether enter next step?'):
                        na_mi_artificial_intelligent(na_mi_search_content=transmit_na_mi_input)

                        if messagebox.askyesno('Attention','whether store data?'):
                            data_part()


                else:
                    logger.error('transmit_na_mi_search failed')

            def quit_transmit_na_mi_search():
                if messagebox.askyesno('Tips', 'Be sure close window?'):
                    na_mi_artificial_option___root.destroy()

            na_mi_artificial_option___root = tkinter.Tk()
            na_mi_artificial_option___root.title('na_mi_artificial_window')

            ttk.Label(na_mi_artificial_option___root, text='input:').grid(row=1, column=0, columnspan=2)

            transmit_na_mi = tkinter.Entry(na_mi_artificial_option___root)
            transmit_na_mi.insert(0, 'Clear content to input ...')
            transmit_na_mi.grid(row=1, column=3, columnspan=5)

            ttk.Button(na_mi_artificial_option___root, text='start_search', command=transmit_na_mi_search).grid(row=2,
                                                                                                                column=0,
                                                                                                                columnspan=2)
            ttk.Button(na_mi_artificial_option___root, text='quit', command=quit_transmit_na_mi_search).grid(row=2,
                                                                                                             column=4,
                                                                                                             columnspan=2)
            na_mi_artificial_option___root.mainloop()

    def wen_xin_artificial_option(self):
        logger.info('wen_xin_artificial_option running.......')
        if messagebox.askyesno('Tips', 'Be sure about your option?'):
            self.equal_root.destroy()
            def transmit_wen_xin_search():
                wen_xin_param = str(get_wen_xin_param.get().strip())
                if len(wen_xin_param) == 0:
                    messagebox.showwarning('Error', 'invalid input')
                elif len(wen_xin_param) != 0:
                    if messagebox.askyesno('Tips', 'whether enter next step?'):
                        wen_xin_artificial_intelligent(wen_xin_search_content=wen_xin_param)

                        if messagebox.askyesno('Attention','whether store data?'):
                            data_part()

                else:
                    logger.error('wen_xin_artificial_search failed')

            def quit_wen_xin_artificial_search():
                if messagebox.askyesno('Tips', 'Be sure close window?'):
                    wen_xin_artificial_option___root.destroy()

            wen_xin_artificial_option___root = tkinter.Tk()
            wen_xin_artificial_option___root.title('wen_xin_artificial_window')

            ttk.Label(wen_xin_artificial_option___root, text='input:').grid(row=1, column=0, columnspan=2)
            get_wen_xin_param = tkinter.Entry(wen_xin_artificial_option___root)
            get_wen_xin_param.insert(0, 'Clear content to input ...')
            get_wen_xin_param.grid(row=1, column=3, columnspan=5)

            ttk.Button(wen_xin_artificial_option___root, text='start_search', command=transmit_wen_xin_search).grid(
                row=3, column=0, columnspan=2)
            ttk.Button(wen_xin_artificial_option___root, text='quit', command=quit_wen_xin_artificial_search).grid(
                row=3, column=3, columnspan=2)
            wen_xin_artificial_option___root.mainloop()

    def dou_bao_artificial_option(self):
        logger.info('dou_bao_artificial_option running.......')
        if messagebox.askyesno('Tips', 'Be sure about your option?'):
            self.equal_root.destroy()
            def transmit_dou_bao_artificial_search():
                dou_bao_param = str(get_dou_bao_param.get().strip())
                if len(dou_bao_param) == 0:
                    messagebox.showwarning('Error', 'invalid input')
                elif len(dou_bao_param) != 0:
                    if messagebox.askyesno('Tips', 'whether enter next step?'):
                        dou_bao_artificial_intelligent(dou_bao_search_content=dou_bao_param)

                        if messagebox.askyesno('Attention','whether store data?'):
                            data_part()

                else:
                    logger.error('dou_bao_artificial_search failed')

            def quit_dou_bao_artificial_search():
                if messagebox.askyesno('Tips', 'Be sure close window?'):
                    dou_bao_artificial_option___root.destroy()

            dou_bao_artificial_option___root = tkinter.Tk()
            dou_bao_artificial_option___root.title('dou_bao_artificial_window')

            ttk.Label(dou_bao_artificial_option___root, text='input:').grid(row=1, column=0, columnspan=2)
            get_dou_bao_param = tkinter.Entry(dou_bao_artificial_option___root)
            get_dou_bao_param.insert(0, 'Clear content to input ...')
            get_dou_bao_param.grid(row=1, column=3, columnspan=5)

            ttk.Button(dou_bao_artificial_option___root, text='start_search',
                       command=transmit_dou_bao_artificial_search).grid(row=4, column=0, columnspan=2)
            ttk.Button(dou_bao_artificial_option___root, text='quit', command=quit_dou_bao_artificial_search).grid(
                row=4, column=3, columnspan=2)
            dou_bao_artificial_option___root.mainloop()

if __name__ == '__main__':
    root = tkinter.Tk()
    test = ArtificialFrame(equal_root=root,set_title_name='test_title',set_geometry='400x300')
    root.mainloop()
