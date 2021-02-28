Hi, here's my submission for the physician appointment tracking project.

I really enjoyed working on it and please don't hesitate to reach out if you have any questions!

### Steps to install the project:
0. Git clone the repository and `cd` into it
1. Create a virtualenv `python3 -m venv notable-project`
2. Activate the virtualenv: `source notable-project/bin/activate`
3. Install the requirements: `pip install -r requirements.txt`
4. Run the app with `python app.py` in the project home directory.
5. Once you verify that the server is running, you should be able to go to `http://127.0.0.1:5000/` and see the website! (Note: the number differ if you are already using the port on your computer)

### Project Notes
When you land on the homepage from a fresh project installation, both the physicians list and the appointments list will be empty.

You can add new Physicians by clicking on the button and supplying the physician name. For example, you can add "John Smith".

This takes you back to the homepage where John Smith will show up on the list, but he will not have any appointments!

You can click to add a new appointment, where you will need to check John Smith's ID from the list in the homepage (by default it will be 1 if he was your first physician).

After you fill out the appointment information and click submit, it takes you back to the homepage, where you should now see the appointment info!

If you add multiple physicians and appointments, clicking on the physician name should show you the appointments only for that physician. For more information, check the screenshots in the `img/` folder of the project.

Best,
Kareem
