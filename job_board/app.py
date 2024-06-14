from flask import Flask, render_template, request, redirect, url_for
from models import db, JobListing, CandidateProfile, JobApplication

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_board.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def job_list():
    jobs = JobListing.query.all()
    return render_template('job_list.html', jobs=jobs)

@app.route('/job/<int:job_id>')
def job_detail(job_id):
    job = JobListing.query.get(job_id)
    return render_template('job_detail.html', job=job)

@app.route('/apply/<int:job_id>', methods=['GET', 'POST'])
def apply_for_job(job_id):
    if request.method == 'POST':
        user_id = 1
        candidate = CandidateProfile.query.filter_by(user_id=user_id).first()
        application = JobApplication(job_id=job_id, candidate_id=candidate.id)
        db.session.add(application)
        db.session.commit()
        return redirect(url_for('job_detail', job_id=job_id))
    job = JobListing.query.get(job_id)
    return render_template('apply.html', job=job)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    user_id = 1
    profile = CandidateProfile.query.filter_by(user_id=user_id).first_or_404()
    if request.method == 'POST':
        profile.bio = request.form.get('bio')
        profile.resume = request.form.get('resume')
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template('profile.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)
