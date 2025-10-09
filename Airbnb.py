# simple_airbnb_basic_full.py
# Simple Airbnb analysis with 'basic' vs. 'full' modes
# Now includes plotting for comparisons in 'full' mode (requires: pip install matplotlib)

import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    path = input("Enter full path to your Airbnb Excel file: ").strip()
    try:
        df = pd.read_excel(path)
        print("✅ File loaded successfully!\n")
        # Basic column validation
        required_cols = ['price']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            print(f"⚠️ Warning: Missing required columns: {missing_cols}. Basic analysis may be limited.\n")
        
        optional_cols = ['room type', 'neighbourhood group']
        missing_optional = [col for col in optional_cols if col not in df.columns]
        if missing_optional:
            print(f"ℹ️ Note: Missing optional columns for full analysis: {missing_optional}. Full mode will skip those sections.\n")
    except Exception as e:
        print(f"❌ File not found or error loading: {e}. Using sample data...\n")
        df = pd.DataFrame({
            'price': [100, 75, 200, 150, 80, 120, 90, 300, 60, 180],
            'room type': ['Entire home/apt'] * 5 + ['Private room'] * 5,
            'neighbourhood group': ['Manhattan'] * 3 + ['Brooklyn'] * 4 + ['Queens'] * 3
        })
    return df

def basic_analysis(df):
    print("📊 BASIC ANALYSIS RESULTS:")
    print(f"Total properties: {len(df)}")
    if 'price' in df.columns:
        print(f"Average price: ${df['price'].mean():.2f}")
        print(f"Cheapest: ${df['price'].min():.2f}")
        print(f"Most expensive: ${df['price'].max():.2f}")
    else:
        print("No 'price' column found. Cannot compute price stats.")

def plot_price_distribution(df):
    """Plot histogram of overall price distribution."""
    if 'price' not in df.columns:
        print("⚠️ No 'price' column for histogram. Skipping.")
        return
    
    plt.figure(figsize=(10, 6))
    plt.hist(df['price'], bins=10, edgecolor='black', alpha=0.7)
    plt.title('Price Distribution of Airbnb Properties')
    plt.xlabel('Price ($)')
    plt.ylabel('Number of Properties')
    plt.grid(True, alpha=0.3)
    plt.savefig('price_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("📈 Price distribution histogram saved as: price_distribution.png")

def plot_by_room_type(df):
    """Bar chart: Average price by room type."""
    if 'room type' not in df.columns or 'price' not in df.columns:
        print("⚠️ Missing 'room type' or 'price' column. Skipping room type plot.")
        return
    
    room_summary = df.groupby('room type')['price'].agg(['mean', 'count']).reset_index()
    room_summary.columns = ['room type', 'avg_price', 'count']
    
    plt.figure(figsize=(8, 5))
    bars = plt.bar(room_summary['room type'], room_summary['avg_price'], color='skyblue', edgecolor='navy')
    plt.title('Average Price by Room Type')
    plt.xlabel('Room Type')
    plt.ylabel('Average Price ($)')
    plt.xticks(rotation=45)
    
    # Add count labels on bars
    for bar, count in zip(bars, room_summary['count']):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, f'n={count}', 
                 ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('room_type_prices.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("📈 Room type comparison bar chart saved as: room_type_prices.png")

def plot_by_neighbourhood(df):
    """Bar chart: Average price by neighbourhood group."""
    if 'neighbourhood group' not in df.columns or 'price' not in df.columns:
        print("⚠️ Missing 'neighbourhood group' or 'price' column. Skipping location plot.")
        return
    
    loc_summary = df.groupby('neighbourhood group')['price'].agg(['mean', 'count']).reset_index()
    loc_summary.columns = ['neighbourhood group', 'avg_price', 'count']
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(loc_summary['neighbourhood group'], loc_summary['avg_price'], color='lightgreen', edgecolor='darkgreen')
    plt.title('Average Price by Neighbourhood Group')
    plt.xlabel('Neighbourhood Group')
    plt.ylabel('Average Price ($)')
    plt.xticks(rotation=45)
    
    # Add count labels on bars
    for bar, count in zip(bars, loc_summary['count']):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, f'n={count}', 
                 ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('neighbourhood_prices.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("📈 Neighbourhood comparison bar chart saved as: neighbourhood_prices.png")

def full_analysis(df):
    print("📊 FULL ANALYSIS RESULTS:")
    # Include basic stats first
    print(f"Total properties: {len(df)}")
    if 'price' in df.columns:
        print(f"Average price: ${df['price'].mean():.2f}")
        print(f"Cheapest: ${df['price'].min():.2f}")
        print(f"Most expensive: ${df['price'].max():.2f}")
    else:
        print("No 'price' column found. Cannot compute price stats.")
    
    # Room type breakdown
    if 'room type' in df.columns:
        print("\n🏠 BREAKDOWN BY ROOM TYPE:")
        room_groups = df.groupby('room type')
        if len(room_groups) > 0:
            for rt, group in room_groups:
                if 'price' in df.columns:
                    avg_price = group['price'].mean()
                    print(f"  {rt}: {len(group)} properties, average ${avg_price:.2f}")
                else:
                    print(f"  {rt}: {len(group)} properties")
        else:
            print("  No data available for room types.")
    else:
        print("\n⚠️ No 'room type' column found. Skipping room type breakdown.")
    
    # Location breakdown
    if 'neighbourhood group' in df.columns:
        print("\n🗺️ BREAKDOWN BY NEIGHBOURHOOD GROUP:")
        loc_groups = df.groupby('neighbourhood group')
        if len(loc_groups) > 0:
            for loc, group in loc_groups:
                if 'price' in df.columns:
                    avg_price = group['price'].mean()
                    print(f"  {loc}: {len(group)} properties, average ${avg_price:.2f}")
                else:
                    print(f"  {loc}: {len(group)} properties")
        else:
            print("  No data available for neighbourhood groups.")
    else:
        print("\n⚠️ No 'neighbourhood group' column found. Skipping location breakdown.")
    
    # Generate plots (only in full mode)
    print("\n🔍 Generating comparison plots...")
    plot_price_distribution(df)
    plot_by_room_type(df)
    plot_by_neighbourhood(df)

def main():
    df = load_data()
    mode = input("Enter mode ('basic' or 'full'): ").strip().lower()
    print()
    if mode == 'basic':
        basic_analysis(df)
    elif mode == 'full':
        full_analysis(df)
    else:
        print("❌ Unknown mode. Defaulting to basic analysis.")
        basic_analysis(df)  # Default to basic if invalid input
    
    # Save results (always, unless explicitly handled)
    output_file = 'simple_airbnb_results.csv'
    df.to_csv(output_file, index=False)
    print(f"\n✅ Analysis complete! Results saved to: {output_file}")

if __name__ == "__main__":
    main()
