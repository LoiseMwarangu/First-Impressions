from app.models import Comment, User,Pitch
from app import db
import unittest

class PitchTest(unittest.TestCase):
    def setUp(self):
        '''
        set up will run before every test
        '''
        self.new_pitch = Pitch(id = 123, pitch_title = 'Pitch', pitch_content = 'Pitch content',category = 'pickup',likes = 0, dislikes = 0)

    def tearDown(self):
        '''
        test case to check if new instance is created
        '''
        User.query.delete()
        Pitch.query.delete()
        Comment.query.delete()

    def test_check_instance(self):
        '''
        test case to check if new instance is created
        '''
        self.assertEquals(self.new_pitch.pitch_title,'Pitch')
        self.assertEquals(self.new_pitch.pitch_content,'Pitch content')
        self.assertEquals(self.new_pitch.category,"pickup")

    def test_save_pitch(self):
        '''
        test case to check if new instance is saved
        '''
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all()) > 0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        pitch = Pitch.get_pitch(123)
        self.assertTrue(pitch is not None)