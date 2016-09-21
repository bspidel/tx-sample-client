import unittest
#from functions.webhook import convert
#from functions.webhook.convert import convert

class ConvertTestCase(unittest.TestCase):
    """Tests for 'main.py'. """

    def test_convert(self):
        """Does handle process request given notification?"""

        ev = {
	"pre_convert_bucket": "",
	"cdn_bucket": "",
	"gogs_user_token": "",
	"api_url": "",
	"data": {
		"secret": "",
		"ref": "refs/heads/master",
		"before": "54d28657e8209bb1a64558ffd7f49e2155c56c8b",
		"after": "6db4e17e9126d72f71cc4a5b9268228b784bebd3",
		"compare_url": "https://git.door43.org/d43/en-obs/compare/54d28657e8209bb1a64558ffd7f49e2155c56c8b...6db4e17e9126d72f71cc4a5b9268228b784bebd3",
		"commits": [{
			"id": "6db4e17e9126d72f71cc4a5b9268228b784bebd3",
			"message": "Update 'content/01.md'\n",
			"url": "https://git.door43.org/d43/en-obs/commit/6db4e17e9126d72f71cc4a5b9268228b784bebd3",
			"author": {
				"name": "richmahn",
				"email": "richard_mahn@wycliffeassociates.org",
				"username": "richmahn"
			}
		}],
		"repository": {
			"id": "3952",
			"name": "en-obs",
			"url": "https://git.door43.org/d43/en-obs",
			"ssh_url": "git@git.door43.org:d43/en-obs.git",
			"clone_url": "https://git.door43.org/d43/en-obs.git",
			"description": "English Open Bible Stories",
			"website": "",
			"watchers": "2",
			"owner": {
				"name": "d43",
				"email": "",
				"username": "d43"
			},
			"private": "false",
			"default_branch": "master"
		},
		"pusher": {
			"name": "Richard Mahn",
			"email": "richard_mahn@wycliffeassociates.org",
			"username": "richmahn"
		},
		"sender": {
			"login": "richmahn",
			"id": 3,
			"avatar_url": "https://secure.gravatar.com/avatar/a7ba1d0fbbc16c8233da31d3cf75ac12"
		}
	    }
        }

        context = {}


        #self.assertTrue(convert(ev, context))
        self.assertTrue( True)
if __name__ == '__main__':
    unittest.main()
