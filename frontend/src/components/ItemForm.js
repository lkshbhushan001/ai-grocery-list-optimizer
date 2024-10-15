import React, { useState } from 'react';
import axios from '../api/api';

function ItemForm() {
  const [item, setItem] = useState({
    name: '',
    quantity: '',
    price: '',
    expiration_date: ''
  });

  const handleChange = (e) => {
    setItem({
      ...item,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/items', item).then((response) => {
      console.log('Item added:', response.data);
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Item Name:
        <input type="text" name="name" value={item.name} onChange={handleChange} />
      </label>
      <label>
        Quantity:
        <input type="number" name="quantity" value={item.quantity} onChange={handleChange} />
      </label>
      <label>
        Price:
        <input type="number" name="price" value={item.price} onChange={handleChange} />
      </label>
      <label>
        Expiration Date:
        <input type="date" name="expiration_date" value={item.expiration_date} onChange={handleChange} />
      </label>
      <button type="submit">Add Item</button>
    </form>
  );
}

export default ItemForm;
