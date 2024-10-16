import React, { useState } from 'react';
import { createItem, updateItem } from '../api/api';

const ItemForm = ({ currentItem, setCurrentItem }) => {
  const [name, setName] = useState(currentItem ? currentItem.name : '');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (currentItem) {
        await updateItem(currentItem.id, { name });
      } else {
        await createItem({ name });
      }
      setCurrentItem(null);  // Reset after creating/updating
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="text" 
        value={name} 
        onChange={(e) => setName(e.target.value)} 
        placeholder="Item name" 
        required 
      />
      <button type="submit">{currentItem ? 'Update' : 'Add'} Item</button>
    </form>
  );
};

export default ItemForm;
