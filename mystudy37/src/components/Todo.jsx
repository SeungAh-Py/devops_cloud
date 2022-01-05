function Todo({ todo, onClick }) {
  return (
    <div>
      <h2 onClick={onClick}>{todo.content}</h2>
    </div>
  );
}

export default Todo;
