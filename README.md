# HW1

(1) How to stepup and run your program: 

  # Part. 1 : Import module
    ．import csv 函式庫：用來處理.csv類型的檔案

  # Part. 2 : Read cwb weather data
    ．將108011244.csv中的資料匯入一個名為data的list中，在data中的元素為一個dictionary而每個dictionary代表108011244.csv中的一橫列。
    ．新增一個名為target_data的list作為輸出用，並初始化target_data = [['目標測站編號#1', 'None'], 
                                                                   ['目標測站編號#2', 'None'],
                                                                   ['目標測站編號#3', 'None'],
                                                                   ['目標測站編號#4', 'None'],
                                                                   ['目標測站編號#5', 'None']]

  # Part. 3 : Data analysis
    ．從data中逐一取出一筆資料做分析：             
        〔分析該資料的測站是否為目標測站〕
        ->否：此筆資料非目標資料，分析下一筆資料
        ->是：〔分析該資料的TEMP是否為'-99.000'或'-999.000'〕
              ->是：此筆資料為無效資料，分析下一筆資料
              ->否：〔分析在target_data中該資料所對應目標測站的TEMP是否為'None'〕
                    ->是：直接將target_data中該資料所對應目標測站的TEMP更改為該資料該資料的TEMP
                    ->否：比較target_data和該資料的TEMP何者較大，將較大者以float類型保存於target_data中，接著分析下一筆資料

  # Part. 4 ： Output result
    ．將target_data輸出

(2) What are the results:
  
  [['C0A880', 28.7], ['C0F9A0', 27.8], ['C0G640', 28.0], ['C0R190', 31.1], ['C0X260', 28.2]]
