SESSION_DURATION = 5

WELCOME = "Hello there! You can use my funky functionality to be even more happy with bunq!"
UPDATE = "You spent {} Euro of your {} budget {}"

CANCEL = "You canceled the process. Will delete all information."
INVALID_INPUT = "Some of the information you gave were incorrect. Try again :-("
INVALID_INPUT_NUMBER = "Invalid input. Please enter a number."
NO_PERMISSION = "You don't have permission to contact this bot!"
ERROR = "Sorry, but an error occurred on my side."

HOME = "Welcome to the Home menu. Where do you want to go?"
ACCOUNT = "Here are some Account functions:"
FUNCTIONS = "Here is what I can do for you:"

DELETE_MSG = "For security, please delete the previous message containing the {}.\n" \
             "\n" \
             "*On iOS:*\n" \
             "\t1. Press long on message\n" \
             "\t2. Click *More...*\n" \
             "\t3. Click *Trash* icon\n" \
             "\t4. Click *Delete for me and bunqBetterBot*\n" \
             "\n" \
             "*On macOS:*\n" \
             "\t1. Right click message\n" \
             "\t2. Check *Delete for bunqBetterBot*\n" \
             "\t3. Click *Delete*\n" \
             "\n" \
             "*On Android:*\n" \
             "\tI have no clue. Check Google."

REGISTER_START = "You want to register! Great!\n"
REGISTER_ENV = "Tell me whether this is a Sandbox or Production account:"
REGISTER_KEY = "Now, please send me your API key:"
REGISTER_PASS = "And finally, to protect your account, send me a secure password:"
REGISTER_END = "Account created! Congratulations!\n" \
               "Press Login to create a session."

LOGIN_START = "Please send me your password:"
LOGIN_FAIL = "Sorry, you either don't have an account yet, or you used the wrong password.\n\n"\
             "Please either create an account first, or try another password."
LOGIN_END = f"You're logged in!\n\n" \
            f"Your session will last {SESSION_DURATION} min before you have to log in again."

CREATE_START = "You want to create a new Budget! Great! Let's get going right away"
CREATE_NAME = "Please enter a name for the new Budget"
CREATE_IBAN = "Next, select the accounts, which the Budget should monitor and click 'Done' when " \
              "you're finished."
CREATE_DURATION = "How many days should the new Budget cover?"
CREATE_DURATION_MORE = "Enter a number for how many days the Budget should cover"
CREATE_FINISH = "Congratulations! You created a new Budget!"