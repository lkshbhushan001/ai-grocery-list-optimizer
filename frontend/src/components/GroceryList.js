import React, { useEffect, useState } from 'react';
import axios from '../api/api';

function GroceryList() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    axios.get('/items').then((response) => setItems(response.data));
  }, []);

  return (
    <div>
      <h1>Grocery List</h1>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            {item.name} - {item.quantity} pcs - ${item.price}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default GroceryList;
