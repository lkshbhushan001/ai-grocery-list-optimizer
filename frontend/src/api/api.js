const API_URL = 'http://localhost:5000';

export const getItems = async () => {
  const response = await fetch(`${API_URL}/items`);
  return response.json();
};

export const createItem = async (item) => {
  const response = await fetch(`${API_URL}/items`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(item),
  });
  return response.json();
};

export const updateItem = async (item) => {
    const response = await fetch(`${API_URL}/items`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(item),
    });
    return response.json();
  };

  export const deleteItem = async (item) => {
    const response = await fetch(`${API_URL}/items`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(item),
    });
    return response.json();
  };
