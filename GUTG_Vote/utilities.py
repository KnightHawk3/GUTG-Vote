import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from GUTG_Vote.models import User, Game

json_key = json.load(open('auth.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                            bytes(json_key['private_key'],
                                            'UTF-8'), scope)
gc = gspread.Client(auth=credentials)
gc.login()
sheet = gc.open_by_key('1ele3BSmZMKWpunF0f3L0_Eeye7ELqtbrb7W89vdtAdk')

def sync_mongo_with_spreadsheet():
    registrants = sheet.worksheet('Registrants').get_all_values()
    registrants.pop(0)
    User.objects.delete()
    for user in registrants:
        if user[1] is not '':
            User(username=user[1], password=user[2]).save()
    wishlist = sheet.worksheet('Wishlist').get_all_values()
    wishlist.pop(0)
    Game.objects.delete()
    for ittr, game in enumerate(wishlist):
        if game[0] is not '':
            Game(title=game[0], url=game[1], votes=int(game[2]), cost=float(game[3]), game_id=int(ittr)).save()

def sync_spreadsheet_with_mongo():
    wishlist = sheet.worksheet('Wishlist')
    for ittr, game in enumerate(Game.objects):
        wishlist.update_cell(ittr + 2, 1, str(game.title))
        wishlist.update_cell(ittr + 2, 2, game.url)
        wishlist.update_cell(ittr + 2, 3, game.votes)
        wishlist.update_cell(ittr + 2, 4, game.cost)