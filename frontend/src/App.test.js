import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import axios from 'axios';
import App from './App';

jest.mock('axios');

describe('App', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('renders the main heading', () => {
    axios.get.mockResolvedValue({ data: { specialties: [] } });
    render(<App />);
    const heading = screen.getByText(/Find Your Contractor/i);
    expect(heading).toBeInTheDocument();
  });

  test('fetches and displays specialties on mount', async () => {
    const mockSpecialties = ['electrician', 'plumber', 'gas', 'builder'];
    axios.get.mockResolvedValueOnce({ data: { specialties: mockSpecialties } });
    axios.get.mockResolvedValueOnce({ data: [] });

    render(<App />);

    await waitFor(() => {
      expect(axios.get).toHaveBeenCalledWith(
        expect.stringContaining('/api/specialties')
      );
    });
  });

  test('fetches contractors on mount', async () => {
    axios.get.mockResolvedValueOnce({ data: { specialties: [] } });
    axios.get.mockResolvedValueOnce({ data: [] });

    render(<App />);

    await waitFor(() => {
      expect(axios.get).toHaveBeenCalledWith(
        expect.stringContaining('/api/contractors'),
        expect.any(Object)
      );
    });
  });

  test('displays contractors when data is loaded', async () => {
    const mockContractors = [
      {
        id: 1,
        name: 'Test Electrician',
        specialty: 'electrician',
        location: 'Sydney',
        latitude: -33.8688,
        longitude: 151.2093,
        price_range: '$$',
        phone: '+61 2 1234 5678',
        email: 'test@example.com',
        description: 'Test description',
      },
    ];

    axios.get.mockResolvedValueOnce({ data: { specialties: [] } });
    axios.get.mockResolvedValueOnce({ data: mockContractors });

    render(<App />);

    await waitFor(() => {
      expect(screen.getByText('Test Electrician')).toBeInTheDocument();
    });
  });

  test('displays no results message when no contractors found', async () => {
    axios.get.mockResolvedValueOnce({ data: { specialties: [] } });
    axios.get.mockResolvedValueOnce({ data: [] });

    render(<App />);

    await waitFor(() => {
      expect(
        screen.getByText(/No contractors found/i)
      ).toBeInTheDocument();
    });
  });

  test('displays error message when API call fails', async () => {
    axios.get.mockResolvedValueOnce({ data: { specialties: [] } });
    axios.get.mockRejectedValueOnce(new Error('API Error'));

    render(<App />);

    await waitFor(() => {
      expect(
        screen.getByText(/Failed to load contractors/i)
      ).toBeInTheDocument();
    });
  });

  test('search button triggers contractor fetch', async () => {
    axios.get.mockResolvedValue({ data: { specialties: [] } });
    axios.get.mockResolvedValue({ data: [] });

    render(<App />);

    const searchButton = screen.getByRole('button', { name: /search/i });
    userEvent.click(searchButton);

    await waitFor(() => {
      expect(axios.get).toHaveBeenCalledTimes(3); // Initial 2 + 1 search click
    });
  });
});
