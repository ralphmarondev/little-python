'''
Enter width of skyscraper: 2
Enter height of skyscraper: 2
 **
****

Enter width of skyscraper: 9
Enter height of skyscraper: 18
     *
 *********
 *********
 *********
 *********
 *********
 *********
 *********
 *********
 *********
 *********
 *********
 *********
 *********
 *********
 *********
 *********
***********

Sample Output 3

Enter width of skyscraper: 10
Enter height of skyscraper: 15
     **
 **********
 **********
 **********
 **********
 **********
 **********
 **********
 **********
 **********
 **********
 **********
 **********
 **********
************
'''
def print_pattern(w, h):
    # if width = odd
    if w % 2 != 0:
        mid = int(w // 2) + 1
        for i in range(h):
            if i == 0:
                print(' ' * mid + '*')
            elif i == h - 1:
                print('*' * (w + 2))
                break
            else:
                print(' ' + '*' * w + ' ')
        return
    
    # width = even
    mid = int(w // 2)
    for i in range(h):
        if i == 0:
            print(' ' * mid  + '**')
        elif i == h - 1:
            print('*' * (w + 2))
        else:
            print(' ' + '*' * w + ' ')
  

w = int(input('Enter width: '))
h = int(input('Enter height: '))

print_pattern(w, h)
