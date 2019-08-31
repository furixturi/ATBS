tableData = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
'''
The goal is to print the above data as follows:
apples    Alice   dogs
orranges  Bob     cats
cherries  Carol   moose
banana    David   goose
'''

def calc_max_col_widths(table_data):
  return [max([len(item) for item in col]) for col in table_data]

def flip_table(table_data):
  # new_num_cols = len(table_data)
  # new_num_rows = len(table_data[0])
  # table_flipped = []
  # for i in range(new_num_rows):
  #   new_row = []
  #   for j in range(new_num_cols):
  #     new_row.append(table_data[j][i])
  #   table_flipped.append(new_row)
  # print(table_flipped)
  return [[table_data[j][i] for j in range(len(table_data))] for i in range(len(table_data[0]))]

def print_table(table_data):
  max_col_widths = calc_max_col_widths(table_data)
  table_flipped = flip_table(table_data)
  # for i in range(len(table_flipped)):
  #   for j in range(len(table_flipped[i])):
  #     table_flipped[i][j] = table_flipped[i][j].ljust(max_col_widths[j])
  #   print('    '.join(table_flipped[i]))
  [print('    '.join([table_flipped[i][j].ljust(max_col_widths[j]) for j in range(len(table_flipped[i]))])) for i in range(len(table_flipped))]

def print_table_delux(table_data):
  max_col_widths = [max([len(item) for item in col]) for col in table_data]
  table_flipped = [[table_data[j][i] for j in range(len(table_data))] for i in range(len(table_data[0]))]
  [print('    '.join([table_flipped[i][j].ljust(max_col_widths[j]) for j in range(len(table_flipped[i]))])) for i in range(len(table_flipped))]