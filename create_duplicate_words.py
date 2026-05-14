sentence="the cat sat on the mat the cat"
word = sentence.split()
word_count={ }
for i in word:

    if i in word_count:
        word_count[i]= word_count[i]+1    

    
    else:
        word_count[i] = 1

for key,value in word_count.items():
    print(f"{key} : {value}")


        
  





# my_dict = {}
# my_dict["name"] = "Arjun"    # key AND value — always
# ```
# word_count["the"] = word_count["the"] + 1
#         ↑                   ↑            ↑
#     store here          pull the        add 1
#     (left side)         current         to it
#                         value out
# ```

# ---

# **Your explanation in plain English was perfect:**
# ```
# word_count["the"]   → goes into dictionary
#                     → finds key "the"
#                     → pulls out its value (example: 2)

# + 1                 → adds 1 to that value
#                     → gives 3

# word_count["the"] = → stores 3 back into "the"