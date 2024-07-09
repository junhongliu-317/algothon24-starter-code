
import numpy as np

##### TODO #########################################
### RENAME THIS FILE TO YOUR TEAM NAME #############
### IMPLEMENT 'getMyPosition' FUNCTION #############
### TO RUN, RUN 'eval.py' ##########################

nInst = 50
currentPos = np.zeros(nInst)


# return position on day `i` after observing price on day `i`
def mean_rev_pos(theo, prc, current_position):
    # sell
    if prc >= theo:
        # got units to sell
        if current_position:
            current_position = 0
        # no units previously bought.
        # position is flat. hold as is.
    # buy
    else:
        # buy in lots of 20
        if current_position < 500:
            current_position += 50
        # reached 100. hold.

    return current_position

# pre-calculated "theoretical" means
# I know the forecasted value should be E[X[t+1] | F[t]] where F[t] is vector of all prices up to time t
# is: E[X[t+1] | F[t]] = a^(1)X_t 
# in fact: E[X[t+k] | F[t]] = a^(k)X_t (where 'a' is the coefficient of X[t-1])
# but tbh I think as a baseline -- exploiting mean reverting works fine

def getMyPosition(prcSoFar):
    # fair price of each instrument
    fair_price = {
        7: 46.73, # instrum 8
        28: 51.16, # instrum 29
        43: 60.92,
        49: 56.04
    }
    last_prc = prcSoFar[:, -1]
    
    # positions for each instrument on current day
    global currentPos

    # update position
    for i in [7, 28, 43, 49]:
        currentPos[i] = mean_rev_pos(fair_price[i], last_prc[i], currentPos[i])
    
    return currentPos