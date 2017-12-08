
'''Computer Science 105
Professor Cristyn Magnus
Noah Beadle, Freshman Programming Portfolio
'''


def emergencycaller():                                                                              ####Defines function "emergencycaller".  this function is the initial interface for Tempus.
    print("TEMPUS RUNNING")                                                                         #Prints a message to console that Tempus is running.
    print("Stay Calm. Please identify the nature of your emergency.")                               #Prints a message that gives instructions to User
    print("[1] Medical Emergency | [2] Crime Related | [3] Fire Related ")                          #Prints a message that contains a key for User Input
    global emergencyclass                                                                           #Makes the variable "emergencyclass" usable outside of the local function. (global)
    emergencyclass = int(input("Input the corresponding numerical digit of your emergency..."))     #Asks the user for numerical input corresponding to the key printed above.

def contact():                                                                                      ####Defines a function "contact".  This function is designed to contact emergency telephone numbers with use of the Twilio Rest API.
    contactchoice = input("Do you want us to contact Authorities?")                                 #Defines "contactchoice" equal to the user choice to contact authorities.
    if contactchoice == "Yes" or contactchoice == "yes":                                            #Accepts lower and upper versions of an affirmative answer, if true,
        global emergencyaddress                                                                     #Makes the variable "emergencyaddress" usable outside of the local function. (global)
        global emergencydescription                                                                 #Makes the variable "emergencydescription" usable outside of the local function. (global)
        emergencyaddress = input("Enter your address in |State|City|Street|Apartment| format.")     #Asks for address input
        if emergencyclass == 1:                                                                     #If block that contains custom messages for additional input, relating to emergency type...
            emergencydetails = "the patient"
        elif emergencyclass == 2:
            emergencydetails = "the suspect"
        elif emergencyclass == 3:
            emergencydetails = "the fire"
        emergencydescription =  input("please give additional details about" + " " + emergencydetails)   #Asks for additional details that are sent via SMS messaging to the emergency contact.



        from twilio.rest import TwilioRestClient                                                    ###'''This code works with the Twilio Rest API'''###

        account_sid="x"                                            ###Twilio Account Number###
        auth_token="x"                                               ###Twilio Authentication Token###

        client = TwilioRestClient(account_sid, auth_token)
        client.messages.create(body= "TEMPUS USER EMERGENCY ALERT" + "        " + "EMERGENCY TYPE:" + " " + emergencylist[emergencyclass]+ "  " + "LOCATION:" + " " + emergencyaddress + "  " + "DESCRIPTION:" + " " + emergencydescription,
                               to="",from_="")                              ###Twilio message created with predefined global variables "emergencylist, emergency class, emergencyaddress, emergencydescription.###
        print("Tempus has sent your information to the authorities.")                               ###MESSAGE IS CURRENTLY CONFIGURED TO SEND TO NOAH BEADLE'S PERSONAL CELL NUMBER.###

    else :
        print("Please contact your local authorities if deemed necessary. Tempus has not sent any information, upon your request.  If you wish to submit further information,  please proceed.")


def basicinfo():                                                                                    ###Creates a function called "basicinfo."###
    emergencycaller()                                                                               #Call the function "emergencycaller".
    global emergencylist                                                                            #Makes the variable "emergencylist" usable outside of the local function. (global)
    emergencylist = {1:"User selected Medical Emergency.", 2:"User selected Crime related.", 3:"User selected Fire related."} #Prints a message to confirm user selection.
    if emergencyclass in emergencylist.keys():                                                      #If numerical input corresponds to a message from the emergencylist array,  this statement will print that choice.
        print(emergencylist[emergencyclass])
    else:                                                                                           #Otherwise, it will give an error.
        print("error")
    verifier = input("Is this correct? Answer yes or no.")                                          #Verifies user input.
    if verifier == "No" or verifier == "no":                                                        #If not verified,  calls emergencycaller function again.
        emergencycaller()
    else :                                                                                          #otherwise, call contact, which will open the SMS functionality.
        contact()
basicinfo()

