import React from 'react';

function GroceryList({ items }) {
  return (
    <ul>
      {items.map((item, index) => (
        <li key={index}>
          {item.name} - {item.quantity} units - Expires on {item.expiry_date}
        </li>
      ))}
    </ul>
  );
}

export default GroceryList;
