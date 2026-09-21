import sender_stand_request
import data

def test_positive_assert():
    track = sender_stand_request.get_order_track()
    response = sender_stand_request.get_order_by_track(track)
    
    assert response.status_code == 200
