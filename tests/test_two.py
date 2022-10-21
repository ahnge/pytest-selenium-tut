

def test_bla(user1):
    assert user1.username == 'test_user'


def test_bla2(new_user1):
    assert new_user1.username == 'Test_user'


def test_blabla(new_user2):
    print(new_user2.is_staff)
    assert new_user2.is_staff
