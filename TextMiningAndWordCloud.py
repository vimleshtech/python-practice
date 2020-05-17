from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 



# Reads 'Youtube04-Eminem.csv' file
#encoding ="latin-1" :read ascii and unicode 
df = pd.read_csv(r"C:\Users\vkumar15\Downloads\YouTube-Spam-Collection-v1\test.csv", encoding ="latin-1")
#print(df)

comment_words = ' '
stopwords = set(STOPWORDS)
#print(stopwords)

# iterate through the csv file 
for val in df.CONTENT: 
      
    # typecaste each val to string 
    val = str(val) 
  
    # split the value 
    tokens = val.split(' ')  #break the string by space seperator 
      
    # Converts each token into lowercase 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower()  #convert every word to lower case 
          
    for words in tokens: 
         comment_words = comment_words + words + ' '

#print(comment_words)

wordcloud = WordCloud(width = 700, height = 600, 
                background_color ='lime', 
                stopwords = stopwords, 
                min_font_size = 12).generate(comment_words)

# plot the WordCloud image                        
plt.figure(figsize = (7, 6), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off")  #dont' show x and y axis 
plt.tight_layout(pad = 0) #no space   
plt.show()










         
         


