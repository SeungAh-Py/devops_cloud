import { useState } from 'react';
import Todo from './Todo';
import TodoForm from './TodoForm';

const INITIAL_STATE = [
  { content: 'Python' },
  { content: 'Django' },
  { content: 'React' },
];

function TodoList() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);

  const deleteHandler = (todoIndex) => {
    setTodoList(todoList.filter((_, index) => todoIndex !== index));
  };

  return (
    <div>
      <TodoForm />
      {todoList.map((todo, index) => (
        <Todo todo={todo} onClick={() => deleteHandler(index)} />
      ))}
    </div>
  );
}

export default TodoList;
