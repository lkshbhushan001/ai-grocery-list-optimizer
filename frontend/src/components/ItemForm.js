import React, { useState } from 'react';

function ItemForm({ onAddItem }) {
  const [name, setName] = useState('');
  const [quantity, setQuantity] = useState('');
  const [expiryDate, setExpiryDate] = useState('');
  const [usageRate, setUsageRate] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    debugger;
    onAddItem({
      name,
      quantity: parseInt(quantity),
      expiry_date: expiryDate,
      usage_rate: parseFloat(usageRate)
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" placeholder="Item Name" value={name} onChange={e => setName(e.target.value)} />
      <input type="number" placeholder="Quantity" value={quantity} onChange={e => setQuantity(e.target.value)} />
      <input type="date" value={expiryDate} onChange={e => setExpiryDate(e.target.value)} />
      <input type="number" placeholder="Usage Rate (per day)" value={usageRate} onChange={e => setUsageRate(e.target.value)} />
      <button type="submit">Add Item</button>
    </form>
  );
}

export default ItemForm;
