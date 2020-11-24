from flask import Flask,render_template,request,redirect,flash,url_for

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def random_board():
	import Generate_random_board
	solution_grid=Generate_random_board.solution
	question_grid=Generate_random_board.grid
	return render_template('backtracking.html',soln=solution_grid,ques=question_grid)

@app.route('/backtracking',methods=["POST"])
def backtracking():
	return redirect(url_for("random_board"));

if __name__=="__main__":
	app.run()
