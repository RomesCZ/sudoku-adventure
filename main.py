import my_check_v2

#main sudoku matrix
i_matrix = [7,3,0, 0,9,1, 8,0,4,
            0,9,8, 0,7,0, 0,5,0,
            0,0,0, 0,0,6, 0,7,0,
            
            0,0,3, 0,2,0, 9,0,0,
            1,0,0, 3,4,0, 0,8,5,
            0,5,6, 7,0,0, 0,0,3,
            
            0,0,0, 0,3,0, 0,9,6,
            3,6,0, 0,8,7, 2,4,0,
            5,0,2, 9,0,0, 0,0,0
           ]


#list to be filled
#links to main matrix
list_empty = []
#pointer to list_empty
int_list_empty = 0

#print(i_matrix[list_empty[int_list_empty]])

###
def action_plus_1():
  global i_matrix, list_empty, int_list_empty
  #check, if can increment
  if i_matrix[list_empty[int_list_empty]] < 9:
    #smaller, increment
    i_matrix[list_empty[int_list_empty]]+=1
  else:
    #go back and increment
    i_matrix[list_empty[int_list_empty]]=0
    #go back?
    if int_list_empty > 0:
      #possible to go back
      int_list_empty-=1
      action_plus_1()
    else:
      #error
      raise RuntimeError("action_plus_1() -> can't go back")

#dd
#int_list_empty = 2
#for x in range(20):
#  action_plus_1()
#print(i_matrix)

###############
#return number of row and column
def getRowColumn(pozice):
  line = 0 #row
  while pozice > 8: #column
    pozice = pozice - 9
    line+=1
  return [line, pozice] #row, column

###############
#return array
def getRow(rowNum):
  global i_matrix
  retArr = []
  retArr.extend(i_matrix[(rowNum*9):(rowNum*9+9)])
  return retArr

###############
#return array
def getColumn(columnNum):
  global i_matrix
  retArr = []
  for x in range(9):
    poz = columnNum+9*x
    retArr.append(i_matrix[poz])
  return retArr

###############
#return array
def getSquare(squareNum):
  retArr = []
  if squareNum == 0:
    f = 0
  elif squareNum == 1:
    f = 3
  elif squareNum == 2:
    f = 6
  elif squareNum == 3:
    f = 27
  elif squareNum == 4:
    f = 30
  elif squareNum == 5:
    f = 33
  elif squareNum == 6:
    f = 54
  elif squareNum == 7:
    f = 57
  elif squareNum == 8:
    f = 60
  else:
    #error
    raise RuntimeError("getSquare(squareNum) -> out of range")

  for x in range(f,f+27,9):
    #print(x)
    retArr.extend(i_matrix[x:x+3])
  return retArr

###############
#return int
def getSquareNum(row,col):
  if row >= 0 and row <= 2:
    if col >= 0 and col <= 2:
      return 0
    elif col >= 3 and col <= 5:
      return 1
    elif col >= 6 and col <= 8:
      return 2
  elif row >= 3 and row <= 5:
    if col >= 0 and col <= 2:
      return 3
    elif col >= 3 and col <= 5:
      return 4
    elif col >= 6 and col <= 8:
      return 5
  elif row >= 6 and row <= 8:
    if col >= 0 and col <= 2:
      return 6
    elif col >= 3 and col <= 5:
      return 7
    elif col >= 6 and col <= 8:
      return 8
  else:
    #error
    raise RuntimeError("getSquareNum(row,col) -> out of range")
    
###############
#return true/false
def checkList(l):
  l.sort()
  prev = 0
  for x in l:
    if x > 0:
      if x > prev:
        a=0
      else:
        return False
      prev = x
  return True

###############
#return true/false
def checkMatrix():
  global i_matrix
  newMatrix = sorted(i_matrix)
  if newMatrix[0] == 0:
    return False
  else:
    return True

###############
#create/fill global list_empty
def createListEmpty():
  global i_matrix, list_empty
  for x in range(len(i_matrix)):
    if i_matrix[x] == 0:
      list_empty.append(x)

###############
#return true/false
def do_checks():
  global i_matrix, list_empty, int_list_empty
  row_col = getRowColumn(list_empty[int_list_empty])
  row = row_col[0]
  col = row_col[1]
  sq_num = getSquareNum(row,col)
  #print('row:{},col:{},sq:{}'.format(row,col,sq_num))
  if not checkList(getRow(row)):
    return False
  if not checkList(getColumn(col)):
    return False
  if not checkList(getSquare(sq_num)):
    return False
  return True

###############
#print formated matrix
def print_matrix():
  global i_matrix
  print(i_matrix[0:27])
  print(i_matrix[27:54])
  print(i_matrix[54:81])

###################33
def main():
  global i_matrix, list_empty, int_list_empty
  createListEmpty()
  #print(list_empty)
  while (int_list_empty+1) <= len(list_empty):
    action_plus_1()
    #print(i_matrix)
    #valid sudoku?
    bln_do_checks = do_checks()
    #print(bln_do_checks)
    #print(int_list_empty)
    #print('---')
    if bln_do_checks :
      #yes
      if (int_list_empty+1) < len(list_empty): 
        int_list_empty+=1
      elif (int_list_empty+1) == len(list_empty):
        if checkMatrix():
          #print(i_matrix)
          print_matrix()
          return True
      else:
        #error
        raise RuntimeError("main() -> int_list_empty is full")
  
main()
