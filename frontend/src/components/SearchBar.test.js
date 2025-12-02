import { render, screen, fireEvent } from '@testing-library/react';
import SearchBar from './SearchBar';

describe('SearchBar', () => {
  const mockOnSpecialtyChange = jest.fn();
  const mockOnSearch = jest.fn();
  const specialties = ['electrician', 'plumber', 'gas', 'builder'];

  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('renders specialty dropdown', () => {
    render(
      <SearchBar
        specialty=""
        specialties={specialties}
        onSpecialtyChange={mockOnSpecialtyChange}
        onSearch={mockOnSearch}
      />
    );

    expect(screen.getByLabelText(/Contractor Type/i)).toBeInTheDocument();
  });

  test('renders search button', () => {
    render(
      <SearchBar
        specialty=""
        specialties={specialties}
        onSpecialtyChange={mockOnSpecialtyChange}
        onSearch={mockOnSearch}
      />
    );

    expect(screen.getByRole('button', { name: /search/i })).toBeInTheDocument();
  });

  test('renders all specialty options', () => {
    render(
      <SearchBar
        specialty=""
        specialties={specialties}
        onSpecialtyChange={mockOnSpecialtyChange}
        onSearch={mockOnSearch}
      />
    );

    expect(screen.getByText('All Specialties')).toBeInTheDocument();
    expect(screen.getByText('Electrician')).toBeInTheDocument();
    expect(screen.getByText('Plumber')).toBeInTheDocument();
    expect(screen.getByText('Gas')).toBeInTheDocument();
    expect(screen.getByText('Builder')).toBeInTheDocument();
  });

  test('calls onSpecialtyChange when specialty is selected', () => {
    render(
      <SearchBar
        specialty=""
        specialties={specialties}
        onSpecialtyChange={mockOnSpecialtyChange}
        onSearch={mockOnSearch}
      />
    );

    const select = screen.getByLabelText(/Contractor Type/i);
    fireEvent.change(select, { target: { value: 'electrician' } });

    expect(mockOnSpecialtyChange).toHaveBeenCalledWith('electrician');
  });

  test('calls onSearch when search button is clicked', () => {
    render(
      <SearchBar
        specialty=""
        specialties={specialties}
        onSpecialtyChange={mockOnSpecialtyChange}
        onSearch={mockOnSearch}
      />
    );

    const searchButton = screen.getByRole('button', { name: /search/i });
    fireEvent.click(searchButton);

    expect(mockOnSearch).toHaveBeenCalledTimes(1);
  });

  test('displays selected specialty', () => {
    render(
      <SearchBar
        specialty="plumber"
        specialties={specialties}
        onSpecialtyChange={mockOnSpecialtyChange}
        onSearch={mockOnSearch}
      />
    );

    const select = screen.getByLabelText(/Contractor Type/i);
    expect(select.value).toBe('plumber');
  });
});
