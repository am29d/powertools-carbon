export type CartCheckedOutEvent = {
  customerId: string;
  cartState: string;
  items: {
    id: string;
    name: string;
    price: number;
    quantity: number;
  }[];
};


export type Request = {
  user: string;
  productId: string;
};

export type Response = {
  [key: string]: unknown;
};

export type SubscriptionResult = {
  id: string;
  productId: string;
};