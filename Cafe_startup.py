import pickle
a=open('Menu_A_C.dat','wb')
list_shop={'Coffee':[['Kohi Americano','100','110'],
                     ['Tokyo Cappucino','110','120'],
                     ['Caffe Latte','110','120']],
           'Tea':[['Hakone Jasmine Tea','75','80'],
                  ['Chamomile Tea','80','85'],
                  ['Matcha Latte','90','100']],
           'Hot Choco':[['Signature Hot Chocolate','100','120'],
                        ['Vanilla Chocolate','110','120']],
           'Iced Beverages':[['Iced Tokyo Kohi','140','150'],
                             ['Iced Macadamia','130','140'],
                             ['Iced Mochaccino','130','140'],
                             ['Iced Macchiato','130','140']]}
pickle.dump(list_shop,a)
a.close()
print('Done')
o_o=open('moni.txt','w')
o_o.write('0')
o_o.close()
