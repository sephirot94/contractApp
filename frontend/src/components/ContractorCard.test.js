import { render, screen } from '@testing-library/react';
import ContractorCard from './ContractorCard';

describe('ContractorCard', () => {
  const mockContractor = {
    id: 1,
    name: 'Test Electrician',
    specialty: 'electrician',
    location: 'Sydney CBD',
    latitude: -33.8688,
    longitude: 151.2093,
    price_range: '$$',
    phone: '+61 2 1234 5678',
    email: 'test@example.com',
    description: 'Professional electrical services',
  };

  test('renders contractor name', () => {
    render(<ContractorCard contractor={mockContractor} />);
    expect(screen.getByText('Test Electrician')).toBeInTheDocument();
  });

  test('renders contractor specialty', () => {
    render(<ContractorCard contractor={mockContractor} />);
    expect(screen.getByText('Electrician')).toBeInTheDocument();
  });

  test('renders contractor location', () => {
    render(<ContractorCard contractor={mockContractor} />);
    expect(screen.getByText('Sydney CBD')).toBeInTheDocument();
  });

  test('renders contractor price range', () => {
    render(<ContractorCard contractor={mockContractor} />);
    expect(screen.getByText('$$')).toBeInTheDocument();
  });

  test('renders contractor description', () => {
    render(<ContractorCard contractor={mockContractor} />);
    expect(screen.getByText('Professional electrical services')).toBeInTheDocument();
  });

  test('renders phone contact link when phone is provided', () => {
    render(<ContractorCard contractor={mockContractor} />);
    const phoneLink = screen.getByText(/Call/i).closest('a');
    expect(phoneLink).toHaveAttribute('href', 'tel:+61 2 1234 5678');
  });

  test('renders email contact link when email is provided', () => {
    render(<ContractorCard contractor={mockContractor} />);
    const emailLink = screen.getByText(/Email/i).closest('a');
    expect(emailLink).toHaveAttribute('href', 'mailto:test@example.com');
  });

  test('renders distance when provided', () => {
    const contractorWithDistance = { ...mockContractor, distance: 5.5 };
    render(<ContractorCard contractor={contractorWithDistance} />);
    expect(screen.getByText(/5.5 km away/i)).toBeInTheDocument();
  });

  test('does not render distance when not provided', () => {
    render(<ContractorCard contractor={mockContractor} />);
    expect(screen.queryByText(/km away/i)).not.toBeInTheDocument();
  });

  test('does not render phone link when phone is not provided', () => {
    const contractorWithoutPhone = { ...mockContractor, phone: null };
    render(<ContractorCard contractor={contractorWithoutPhone} />);
    expect(screen.queryByText(/Call/i)).not.toBeInTheDocument();
  });

  test('does not render email link when email is not provided', () => {
    const contractorWithoutEmail = { ...mockContractor, email: null };
    render(<ContractorCard contractor={contractorWithoutEmail} />);
    expect(screen.queryByText(/Email/i)).not.toBeInTheDocument();
  });

  test('renders correct specialty icon for electrician', () => {
    render(<ContractorCard contractor={mockContractor} />);
    expect(screen.getByText('⚡')).toBeInTheDocument();
  });

  test('renders correct specialty icon for plumber', () => {
    const plumber = { ...mockContractor, specialty: 'plumber' };
    render(<ContractorCard contractor={plumber} />);
    expect(screen.getByText('🔧')).toBeInTheDocument();
  });

  test('renders correct specialty icon for gas fitter', () => {
    const gasFitter = { ...mockContractor, specialty: 'gas' };
    render(<ContractorCard contractor={gasFitter} />);
    expect(screen.getByText('🔥')).toBeInTheDocument();
  });

  test('renders correct specialty icon for builder', () => {
    const builder = { ...mockContractor, specialty: 'builder' };
    render(<ContractorCard contractor={builder} />);
    expect(screen.getByText('🏗️')).toBeInTheDocument();
  });
});
