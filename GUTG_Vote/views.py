from flask import Blueprint, redirect, url_for, request, render_template, flash, g
from flask.ext.login import login_user, logout_user, current_user, login_required

from GUTG_Vote import utilities
from GUTG_Vote.models import User, Game
from GUTG_Vote.forms import LoginForm
from GUTG_Vote.extensions import db

main = Blueprint('main', __name__)

@main.before_request
def before_request():
    g.user = current_user

@main.route('/')
def index():
    return render_template('index.html', games=Game.objects.order_by('votes'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        registered_user = User.objects(
            username=form.username.data,
            password=form.password.data).first()
        login_user(registered_user, remember=form.remember_me.data)
        flash("Logged in Sucessfully", 'info')
        return redirect(request.args.get("next") or url_for("main.index"))
    return render_template('login.html', form=form)


@main.route('/logout')
def logout():
    logout_user()
    flash("Logged out Sucessfully", 'info')
    return redirect(url_for('main.index')) 

@main.route('/<game_id>/vote', methods=['POST'])
@login_required
def vote_comment(game_id):
    game = Game.objects(game_id=game_id).first()
    print(current_user)
    print(game)
    if current_user.username not in game.voters:
        game.votes += 1
        game.voters.append(current_user.username)
        game.save()
        utilities.sync_spreadsheet_with_mongo()
        return str(game.votes)
    else:
        return "Already Voted"