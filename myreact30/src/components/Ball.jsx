const Ball = ({number}) => {
    let backgroundColor;
    if (number <= 10) {
        backgroundColor = 'yellow';
    } else if (number <= 20) {
        backgroundColor = 'blue';
    } else if (number <= 30) {
        backgroundColor = 'red';
    } else if (number <= 40) {
        backgroundColor = 'gray';
    } else {
        backgroundColor = 'yellow';
    }
    return (
        <div 
        className="ball"
        style={{
            ...style,
            backgroundColor: backgroundColor
        }}>
            {number}
        </div>
    );
};

const style = {
    width: '100px',
    height: '100px',
    margin: '10px',
    borderRadius: '50px',
    lineHeight: '100px',
    textAlign: 'center',
    display: 'inline-block',
    fontSize: '3rem',
    userSelect: 'none',
    color: 'white',
};

export default Ball;