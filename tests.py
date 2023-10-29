import py_cui

from dicts import piecesASCII, asciiChars

let = ["","a","b","c","d","e","f","g","h"]
    
class Board:
    def __init__(self, master) -> None:

        self.master = master
        self.g = py_cui.grid.Grid(num_rows=9, num_columns=9, height=200, width=200, logger=None)
        #self.cos = self.master.add_button(asciiChars['b']['p'], 0, 0, row_span = 5, column_span = 9,  command=None, padx = 10, pady = 10)   
        #self.cos = self.master.add_button(asciiChars['b']['p'], 5, 9, row_span = 5, column_span = 9,  command=None)   
        # self.board = []
        # for a in range(9):
        #     tmp = []
        #     for b in range(9):
        #         if(a==0):
        #             tmp.append(self.master.add_button(str(let[b]), a, b, row_span = 1, column_span = 1,  command=None))
        #         elif(b==0):
        #             tmp.append(self.master.add_button(str(a), a, b, row_span = 1, column_span = 1,  command=None))
        #         else:
        #             tmp.append(self.master.add_button(asciiChars['b']['p'], a, b, row_span = 1, column_span = 1,  command=None))
        #     self.board.append(tmp)
        # scroll_menu_options = ['New Game', 'Undo Move', 'Redo Move', 'Exit']
        # self.menu = self.master.add_scroll_menu("Menu", 5,9, row_span = 4, column_span = 4)
        # self.menu.add_item_list(scroll_menu_options)
        # self.menu.add_key_command(py_cui.keys.KEY_ENTER, self.operate_on_menu_item)
        # self.menu.add_key_command(py_cui.keys.KEY_W_LOWER,  command=None)
        # self.menu.add_key_command(py_cui.keys.KEY_A_LOWER,  command=None)
        # self.menu.add_key_command(py_cui.keys.KEY_S_LOWER,  command=None)
        # self.menu.add_key_command(py_cui.keys.KEY_D_LOWER,  command=None)
        # self.menu.set_focus_text('Use WASD to move the board, arrows to select menu items, and enter to use a menu item')

        #self.input_textbox = self.master.add_text_box('Input: ', 9,0, row_span = 1, column_span = 9, pady = 0)

    def operate_on_menu_item(self):
        """Function that operates on the current selected menu item
        """

        operation = self.menu.get()
        if operation == 'New Game':
            #self.initialize_new_game()
            pass
        elif operation == 'Undo Move':
            #self.undo_move(True)
            pass
        elif operation == 'Redo Move':
            #self.undo_move(False)
            pass
        elif operation == 'Exit':
            exit()




# Create the CUI with 7 rows 6 columns, pass it to the wrapper object, and start it
#root = py_cui.PyCUI(9, 13)
root = py_cui.PyCUI(10, 18)
root.set_title('CUI TODO List')
s = Board(root)
root.start()

    #     # The scrolled list cells that will contain our tasks in each of the three categories
    #     self.todo_scroll_cell = self.master.add_scroll_menu('TODO', 0, 0, row_span=6, column_span=2)
    #     self.in_progress_scroll_cell = self.master.add_scroll_menu('In Progress', 0, 2, row_span=7, column_span=2)
    #     self.done_scroll_cell = self.master.add_scroll_menu('Done',  0, 4, row_span=7, column_span=2)

    #     # Textbox for entering new items
    #     self.new_todo_textbox = self.master.add_text_box('TODO Item', 6, 0, column_span=2)

    #     self.new_todo_textbox.add_key_command(py_cui.keys.KEY_ENTER, self.add_item)
    #     self.todo_scroll_cell.add_key_command(py_cui.keys.KEY_ENTER, self.mark_as_in_progress)
    #     self.in_progress_scroll_cell.add_key_command(py_cui.keys.KEY_ENTER, self.mark_as_done)
    #     self.done_scroll_cell.add_key_command(py_cui.keys.KEY_ENTER, self.remove_item)

    # def add_item(self):
    #     """ Add a todo item """

    #     self.todo_scroll_cell.add_item(f'{self.new_todo_textbox.get()}')
    #     self.new_todo_textbox.clear()


    # def mark_as_in_progress(self):
    #     """ Mark a todo item as inprogress. Remove it from todo scroll list, add it to in progress list, or show error popup if no tasks """

    #     in_prog = self.todo_scroll_cell.get()
    #     if in_prog is None:
    #         self.master.show_error_popup('No Item', 'There is no item in the list to mark as in progress')
    #         return
    #     self.todo_scroll_cell.remove_selected_item()
    #     self.in_progress_scroll_cell.add_item(in_prog)


    # def mark_as_done(self):
    #     """ Mark a inprogress item as done. Remove it from inprogress scroll list, add it to done list, or show error popup if no tasks """

    #     done = self.in_progress_scroll_cell.get()
    #     if done is None:
    #         self.master.show_error_popup('No Item', 'There is no item in the list to mark as done')
    #         return
    #     self.in_progress_scroll_cell.remove_selected_item()
    #     self.done_scroll_cell.add_item(done)


    # def remove_item(self):
    #     """ Remove a todo item """

    #     self.done_scroll_cell.remove_selected_item()

