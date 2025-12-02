import { render, screen, fireEvent } from '@testing-library/react';
import LocationInput from './LocationInput';

describe('LocationInput', () => {
  const mockOnLocationChange = jest.fn();
  const mockOnUseCurrentLocation = jest.fn();

  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('renders location input section', () => {
    render(
      <LocationInput
        location={null}
        onLocationChange={mockOnLocationChange}
        onUseCurrentLocation={mockOnUseCurrentLocation}
      />
    );

    expect(screen.getByText('Location')).toBeInTheDocument();
  });

  test('renders "Use Current Location" button', () => {
    render(
      <LocationInput
        location={null}
        onLocationChange={mockOnLocationChange}
        onUseCurrentLocation={mockOnUseCurrentLocation}
      />
    );

    expect(
      screen.getByRole('button', { name: /Use Current Location/i })
    ).toBeInTheDocument();
  });

  test('renders latitude and longitude input fields', () => {
    render(
      <LocationInput
        location={null}
        onLocationChange={mockOnLocationChange}
        onUseCurrentLocation={mockOnUseCurrentLocation}
      />
    );

    expect(screen.getByPlaceholderText(/Latitude/i)).toBeInTheDocument();
    expect(screen.getByPlaceholderText(/Longitude/i)).toBeInTheDocument();
  });

  test('renders "Set Location" button', () => {
    render(
      <LocationInput
        location={null}
        onLocationChange={mockOnLocationChange}
        onUseCurrentLocation={mockOnUseCurrentLocation}
      />
    );

    expect(
      screen.getByRole('button', { name: /Set Location/i })
    ).toBeInTheDocument();
  });

  test('calls onUseCurrentLocation when button is clicked', () => {
    render(
      <LocationInput
        location={null}
        onLocationChange={mockOnLocationChange}
        onUseCurrentLocation={mockOnUseCurrentLocation}
      />
    );

    const button = screen.getByRole('button', { name: /Use Current Location/i });
    fireEvent.click(button);

    expect(mockOnUseCurrentLocation).toHaveBeenCalledTimes(1);
  });

  test('calls onLocationChange with coordinates when Set Location is clicked', () => {
    render(
      <LocationInput
        location={null}
        onLocationChange={mockOnLocationChange}
        onUseCurrentLocation={mockOnUseCurrentLocation}
      />
    );

    const latInput = screen.getByPlaceholderText(/Latitude/i);
    const lonInput = screen.getByPlaceholderText(/Longitude/i);
    const setButton = screen.getByRole('button', { name: /Set Location/i });

    fireEvent.change(latInput, { target: { value: '-33.8688' } });
    fireEvent.change(lonInput, { target: { value: '151.2093' } });
    fireEvent.click(setButton);

    expect(mockOnLocationChange).toHaveBeenCalledWith({
      latitude: -33.8688,
      longitude: 151.2093,
      name: 'Custom Location',
    });
  });

  test('does not call onLocationChange when coordinates are empty', () => {
    render(
      <LocationInput
        location={null}
        onLocationChange={mockOnLocationChange}
        onUseCurrentLocation={mockOnUseCurrentLocation}
      />
    );

    const setButton = screen.getByRole('button', { name: /Set Location/i });
    fireEvent.click(setButton);

    expect(mockOnLocationChange).not.toHaveBeenCalled();
  });

  test('displays current location when provided', () => {
    const location = {
      latitude: -33.8688,
      longitude: 151.2093,
      name: 'Your Location',
    };

    render(
      <LocationInput
        location={location}
        onLocationChange={mockOnLocationChange}
        onUseCurrentLocation={mockOnUseCurrentLocation}
      />
    );

    expect(screen.getByText(/Your Location/i)).toBeInTheDocument();
    expect(screen.getByText(/-33.8688/)).toBeInTheDocument();
    expect(screen.getByText(/151.2093/)).toBeInTheDocument();
  });

  test('renders location hint', () => {
    render(
      <LocationInput
        location={null}
        onLocationChange={mockOnLocationChange}
        onUseCurrentLocation={mockOnUseCurrentLocation}
      />
    );

    expect(screen.getByText(/Sydney CBD/i)).toBeInTheDocument();
  });
});
