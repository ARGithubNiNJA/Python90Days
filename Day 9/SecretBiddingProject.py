#Secret Biding Game
# method to compare the bids
def find_the_highest_bidder(bids):
    winner = ""
    highest_bidder_value = 0

    for bidder in bids:
        current_bid_amount = bids[bidder]

        if current_bid_amount > highest_bidder_value:
            highest_bidder_value = current_bid_amount
            winner = bidder

    print(f"The winner is {winner} and the highest bid amount is ${highest_bidder_value}")

continue_bidding=True
bids_dictionary={}
#looping over the process
while continue_bidding:
    ## Enter the name input
    name = input("Enter your name?\n")

    ## Asking the bid
    value= int(input("Enter Your Bid\n"))

    ## pushing the value in the dictionary
    bids_dictionary[name] = value

    ##Asking if any more items could be added to the dictionary
    should_continue = input("Are there any other bidder in the house\n").lower();

    if should_continue == "no":
        continue_bidding = False
        find_the_highest_bidder(bids_dictionary)




