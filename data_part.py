import textwrap
from cite_parts import write_txt_,write_json_
from loguru import logger
import tkinter
from tkinter import messagebox,ttk

origin_all_possible_data = []

renew_all_possible_data = []

def data_part():
    logger.info('collect_possible_data running...')
    try:
        if len(origin_all_possible_data) == 0:
            logger.error('column_data is none')
        elif len(origin_all_possible_data) != 0:
            logger.info('collecting all data ......')
            for each_element in origin_all_possible_data:
                renew_object_content___ = textwrap.wrap(str(each_element))
                renew_all_possible_data.append(renew_object_content___)
            logger.info('all data collected.')

            def output_txt_format():
                if messagebox.askyesno('Attention', 'creat txt file?'):
                    collect_possible_data___root.destroy()
                    write_txt_(txt_content=renew_all_possible_data, txt_name='collect_txt_format', if_addition='True')

            def output_json_format():
                if messagebox.askyesno('Attention', 'creat json file?'):
                    collect_possible_data___root.destroy()
                    write_json_(json_content=renew_all_possible_data, json_name='collect_json_format')

            def quit_collect_possible_data():
                if messagebox.askyesno('Attention', 'quit?'):
                    collect_possible_data___root.destroy()

            collect_possible_data___root = tkinter.Tk()
            collect_possible_data___root.title('file making')

            ttk.Button(collect_possible_data___root, text='txt', command=output_txt_format).pack()
            ttk.Button(collect_possible_data___root, text='json', command=output_json_format).pack()
            ttk.Button(collect_possible_data___root, text='quit', command=quit_collect_possible_data).pack()
            collect_possible_data___root.mainloop()
    except Exception as e:
        logger.error(e)

if __name__ == '__main__':
    data_part()