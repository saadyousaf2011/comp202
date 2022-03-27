# -*- coding: utf-8 -*-
import praw
import random
import pickle
  
def get_topic_comments(submission):
    ''' (Submission) -> list<Comment>
    
    >>> submission = reddit.submission(url='https://www.reddit.com/r/mcgill/comments/eay2ne/mcgill_subreddit_bingo_finals_edition/')
    >>> get_topic_comments(submission)
    [Comment(id='fb0vh26'), Comment(id='fb0l4dk'), Comment(id='fb15bvy'), Comment(id='fb1pwq8'), Comment(id='fb26drr'), Comment(id='fj2wd6x'), Comment(id='fb1spzv'), Comment(id='fb1td2g'), Comment(id='fb1trul')]
    '''
    comments = []
    
    comments_to_check = submission.comments[:]
    for comment in comments_to_check:
        comments.append(comment)
        comments_to_check.extend(comment.replies)
        #for second_level_comment in comment.replies:
        #    comments.append(second_level_comment)
    return comments

if __name__ == '__main__':
    reddit = praw.Reddit('bot', config_interpolation="basic")
    url = "https://www.reddit.com/r/mcgill/comments/paf85s/the_only_society_we_deserve/"
    submission = reddit.submission(url=url)
    print(submission)
    
    submission.comments.replace_more(limit=None)
    print(submission)
    
    
    #open file to dump
    file = open('submission_obj_part_1_2.pkl', 'wb')
    # dump information to that file
    pickle.dump(submission, file)
    # close the file
    file.close()
    
    #open file to read
    file = open('submission_obj_part_1_2.pkl', 'rb')
    # dump information to that file
    subm = pickle.load(file)
    # close the file
    file.close()

    #print retreived data
    print(subm)

    

