# number-plate-reader

It provides functionality for:

1. Uploading image of a vehicle.
2. Reading its number plate.
3. Returning the response as

```json
{
  "registrationNumber": "HR10A1010"
}
```

### Getting started

Please follow the following steps

1. Navigate to root directory.
1. Run `python3 -m venv venv`
1. Run `source venv/bin/activate` (in case of unix/linux) and for windows \*\*search on internet "how to activate virtual env"
1. Run `pip install -r requirements.txt`
1. Run `python app.py`

Now, you will see that a server has been started and the intial setup is done

Happy coding! 🎉

### Saving changes to remote

**Make sure you are using your own seperate branch (something like: 'dev-{your name}')**

1. Run `pip freeze > requirements.txt` - For this command to run, make sure you have run the four commands of **Getting started** as indicated above.
1. Create a good commit.
1. Push your changes to your branch in remote (may be this command can be used: `git push -u origin dev-{your name}`)
1. On the [github repo page](https://github.com/Avchhikara/number-plate-reader/), create a pull request or contact me (Avnish)

That's all you need to save changes in remote.
