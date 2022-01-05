import Stars from './Stars';

function Review({ review }) {
  return (
    <div>
      <div className="border-1 border-crimson-700 m-1 p-1 hover:bg-blue-200">
        {review.review}
        <Stars rating={review.star} />
      </div>
    </div>
  );
}

export default Review;
