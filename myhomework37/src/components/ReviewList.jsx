import Review from './Review.jsx';
import ReviewForm from './ReviewForm.jsx';
import { useState } from 'react';
import useFieldValues from 'hooks/useFieldValues.js';

const INITIAL_STATE = [
  {
    review: 'inception : Christopher Nolan의 역작',
    star: 5,
  },
  {
    review: 'Eternal Sunshine of the Spotless Mind : Michel Gondry 감독',
    star: 4,
  },
  {
    review: 'Whiplash : 미쳤다',
    star: 5,
  },
  {
    review: '클레멘타인 (2004) : 나만 당할수 없다',
    star: 1,
  },
];

const INITIAL_VALUE = {
  review: '',
  star: 0,
};

function ReviewList() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);
  const [showForm, setShowForm] = useState(false);
  const [fieldValues, handleChange, emptyFieldValues] =
    useFieldValues(INITIAL_VALUE);

  const appendReview = () => {
    setReviewList((prevReviewList) => [...prevReviewList, { ...fieldValues }]);
    setShowForm((prevState) => !prevState);
    emptyFieldValues();
  };

  return (
    <div className="w-[400px] m-auto">
      <h2 className="text-xl border-b-2 border-orange-400">Review List</h2>

      {showForm && (
        <ReviewForm handleSubmit={appendReview} handleChange={handleChange} />
      )}
      {!showForm && (
        <button
          className="text-sm bg-orange-200 hover:bg-orange-300 border rounded-md my-2 p-1"
          onClick={() => setShowForm((prevState) => !prevState)}
        >
          New Review
        </button>
      )}

      {reviewList.map((review) => (
        <Review review={review} />
      ))}
    </div>
  );
}
export default ReviewList;
