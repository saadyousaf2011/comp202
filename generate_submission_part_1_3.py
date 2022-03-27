# -*- coding: utf-8 -*-
import praw
import random
import pickle
  

if __name__ == '__main__':
    reddit = praw.Reddit('bot', config_interpolation="basic")
    url = "https://www.reddit.com/r/mcgill/comments/pa6ntd/does_mcgill_have_a_taylor_swift_society/"
    submission = reddit.submission(url=url)
    print(submission)
    
    submission.comments.replace_more(limit=None)
    print(submission)
    
    
    #open file to dump
    file = open('submission_obj_part_1_3.pkl', 'wb')
    # dump information to that file
    pickle.dump(submission, file)
    # close the file
    file.close()
    
    #open file to read
    file = open('submission_obj_part_1_3.pkl', 'rb')
    # dump information to that file
    subm = pickle.load(file)
    # close the file
    file.close()

    #print retreived data
    print(subm)

    


