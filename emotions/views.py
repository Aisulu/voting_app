from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, logout #,login
from django.db.models import Q
from .models import Vote, User, Tweet
import random



def index(request):

    logged_user = request.user
    
    total_tweets = Tweet.objects

    voted_tweets = set()
    voted_cnt = 0
    for vote in Vote.objects.filter(user_id = request.user.id).select_related('tweet'):
        voted_tweets.add(vote.tweet)
        voted_cnt += 1

    unvoted_tweets = total_tweets

    
    for voted_tweet in voted_tweets:
        unvoted_tweets = unvoted_tweets.exclude(id = voted_tweet.id)
    
    
    
    total_tweets_number = total_tweets.count
    voted_tweets_number = Vote.objects.filter(user_id = request.user.id).count
    unvoted_tweets_number = 997 - voted_cnt #unvoted_tweets.count
    

    context = {'logged_user': logged_user, 'voted_tweets_number': voted_tweets_number, 'unvoted_tweets_number': unvoted_tweets_number, 'voted_tweets': voted_tweets, 'unvoted_tweets': unvoted_tweets, 'request': request}

    return render(request, 'emotions/index.html', context)



def vote(request):



        logged_user = request.user
        
        
        
        total_tweets = Tweet.objects.all()
    
        voted_tweets = set()
        voted_cnt = 0
        for vote in Vote.objects.filter(user_id = request.user.id).select_related('tweet'):
            voted_tweets.add(vote.tweet)
            voted_cnt += 1

        unvoted_tweets = total_tweets

        for voted_tweet in voted_tweets:
            unvoted_tweets = unvoted_tweets.exclude(id = voted_tweet.id)
    
    
    
        total_tweets_number = total_tweets.count
        voted_tweets_number = Vote.objects.filter(user_id = request.user.id).count
        unvoted_tweets_number = 997 - voted_cnt

        if(unvoted_tweets.first()):
            #first_unvoted_tweet_id = random.choice(unvoted_tweets).id
            first_unvoted_tweet_id = unvoted_tweets.first().id

            first_unvoted_tweet = Tweet.objects.get(id = first_unvoted_tweet_id)
            text = first_unvoted_tweet.original_text
            text = text.replace("&amp;", "&")
            first_unvoted_tweet.original_text = text


            context = {'logged_user': logged_user, 'voted_tweets_number': voted_tweets_number, 'unvoted_tweets_number': unvoted_tweets_number, 'voted_tweets': voted_tweets, 'unvoted_tweets': unvoted_tweets, 'request': request, 'first_unvoted_tweet_id': first_unvoted_tweet_id, 'first_unvoted_tweet': first_unvoted_tweet, 'total_tweets_number': total_tweets_number, 'current_tweet_id':first_unvoted_tweet_id}

        else:
            context = {'logged_user': logged_user, 'voted_tweets_number': voted_tweets_number, 'unvoted_tweets_number': unvoted_tweets_number, 'voted_tweets': voted_tweets, 'unvoted_tweets': unvoted_tweets, 'request': request, 'total_tweets_number': total_tweets_number}

            return render(request, 'emotions/index.html', context)
    
        return render(request, 'emotions/vote.html', context)


###############################################################################################
def evaluate(request, first_unvoted_tweet_id):
    logged_user = request.user


    anger = 0
    disgust = 0
    fear = 0
    joy = 0
    sadness = 0
    surprise = 0
    trust = 0
    anticipation = 0

    anger_value = request.POST.get('anger_radio', 1.0)
    disgust_value = request.POST.get('disgust_radio', 1.0)
    fear_value = request.POST.get('fear_radio', 1.0)
    joy_value = request.POST.get('joy_radio', 1.0)
    sadness_value = request.POST.get('sadness_radio', 1.0)
    surprise_value = request.POST.get('surprise_radio', 1.0)
    trust_value = request.POST.get('trust_radio', 1.0)
    anticipation_value = request.POST.get('anticipation_radio', 1.0)

    first_unvoted_tweet = Tweet.objects.get(id = first_unvoted_tweet_id)
    
    
    
    vote = Vote.objects.create(tweet = first_unvoted_tweet,
                               user = logged_user,
                               
                               anger = anger_value,
                               disgust = disgust_value,
                               fear = fear_value,
                               joy = joy_value,
                               sadness = sadness_value,
                               surprise = surprise_value,
                               trust = trust_value,
                               anticipation = anticipation_value

                              )
    
    #question = get_object_or_404(Question, pk=question_id)
    #selected_choice = question.choice_set.get(pk=request.POST['choice'])


    context = {'logged_user': logged_user, 'first_unvoted_tweet_id': first_unvoted_tweet_id, 'first_unvoted_tweet': first_unvoted_tweet}
#return render(request, 'emotions/evaluate.html', context)
    return HttpResponseRedirect(reverse('vote'))


###############################################################################################
def delete(request, first_unvoted_tweet_id):
  
  Tweet.objects.filter(id = first_unvoted_tweet_id).delete()

  logged_user = request.user

  total_tweets = Tweet.objects
    
  voted_tweets = set()
  for vote in Vote.objects.filter(user_id = request.user.id).select_related('tweet'):
      voted_tweets.add(vote.tweet)

  unvoted_tweets = total_tweets

  for voted_tweet in voted_tweets:
      unvoted_tweets = unvoted_tweets.exclude(id = voted_tweet.id)
    
    
    
  total_tweets_number = total_tweets.count
  voted_tweets_number = Vote.objects.filter(user_id = request.user.id).count
  unvoted_tweets_number = unvoted_tweets.count

  if(unvoted_tweets.first()):
      first_unvoted_tweet_id = unvoted_tweets.first().id
      first_unvoted_tweet = Tweet.objects.get(id = first_unvoted_tweet_id)

      context = {'logged_user': logged_user, 'voted_tweets_number': voted_tweets_number, 'unvoted_tweets_number': unvoted_tweets_number, 'voted_tweets': voted_tweets, 'unvoted_tweets': unvoted_tweets, 'request': request, 'first_unvoted_tweet_id': first_unvoted_tweet_id, 'first_unvoted_tweet': first_unvoted_tweet, 'total_tweets_number': total_tweets_number, 'current_tweet_id':first_unvoted_tweet_id}

  else:
      context = {'logged_user': logged_user, 'voted_tweets_number': voted_tweets_number, 'unvoted_tweets_number': unvoted_tweets_number, 'voted_tweets': voted_tweets, 'unvoted_tweets': unvoted_tweets, 'request': request, 'total_tweets_number': total_tweets_number}



  return render(request, 'emotions/vote.html', context)



def logout_view(request):
    logout(request)

    logged_user = request.user
    context = {'logged_user': logged_user}
    return render(request, 'emotions/logout_view.html', context)





def slider(request):
    
    logged_user = request.user
    context = {'logged_user': logged_user}
    return render(request, 'emotions/slider.html', context)






#def on_press(key):
#    print('{0} pressed'.format(
#        key))

#def on_release(key):
#    print('{0} release'.format(
#        key))
#    if key == Key.esc:
         #Stop listener
#        return False

# Collect events until released
#with Listener(
#        on_press=on_press,
#        on_release=on_release) as listener:
#    listener.join()












