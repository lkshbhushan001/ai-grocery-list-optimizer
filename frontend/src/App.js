import React, { useState, useEffect } from 'react';
import GroceryList from './components/GroceryList';
import ItemForm from './components/ItemForm';
import { getItems, createItem } from './api/api';

function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    getItems().then(data => setItems(data));
  }, []);

  const addItem = (item) => {
    createItem(item).then(newItem => setItems([...items, newItem]));
  };

  return (
    <div>
      <h1>Grocery List</h1>
      <ItemForm onAddItem={addItem} />
      <GroceryList items={items} />
    </div>
  );
}

export default App;
