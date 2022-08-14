from flask import Flask, render_template
from utils import get_candidate, get_candidates_by_name, get_candidates_by_skill, load_candidates_from_json
from candidate import Candidate

app = Flask(__name__)


@app.route('/')
def get_all_user():
    candidates:list[Candidate]=load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:x>')
def get_one_candidate(x):
    item: dict = get_candidate(x)
    if not item:
        return "NOT FOUND"
    else:
        return render_template('single.html', item=item)


@app.route('/search/<candidate_name>')
def get_name(candidate_name):
    items: list[Candidate] = get_candidates_by_name(candidate_name)
    if not items:
        return "NOT FOUND"
    else:
        return render_template('search.html', candidates=items)


@app.route('/skill/<skill_name>')
def get_skill(skill_name):
    items: list[Candidate] = get_candidates_by_skill(skill_name)
    if not items:
        return "NOT FOUND"
    else:
        return render_template('skill.html', skill=skill_name, candidates=items)


app.run()
