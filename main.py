import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os
from pathlib import Path


class WeatherDataVisualizer:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.df = None
        self.cleaned_df = None
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)

    def load_and_inspect_data(self):
        print("=" * 70)
        print("TASK 1: DATA ACQUISITION AND LOADING")
        print("=" * 70)
        try:
            self.df = pd.read_csv(self.csv_file_path)
            print(f"\n✓ Successfully loaded {self.csv_file_path}")
            print(
                f"\nDataset Shape: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
            print("\n--- First 5 Rows ---")
            print(self.df.head())
            print("\n--- Data Info ---")
            print(self.df.info())
            print("\n--- Statistical Summary ---")
            print(self.df.describe())
            print("\n--- Missing Values ---")
            print(self.df.isnull().sum())
            return self.df
        except FileNotFoundError:
            print(f"Error: File '{self.csv_file_path}' not found.")
            raise
        except Exception as e:
            print(f"Error loading file: {e}")
            raise

    def clean_and_process_data(self, date_column='Date', temp_column=None,
                               rainfall_column=None, humidity_column=None):
        print("\n" + "=" * 70)
        print("TASK 2: DATA CLEANING AND PROCESSING")
        print("=" * 70)

        if self.df is None:
            print("Error: Data not loaded. Run load_and_inspect_data() first.")
            return

        self.cleaned_df = self.df.copy()
        print(f"\n--- Handling Missing Values ---")
        missing_before = self.cleaned_df.isnull().sum().sum()
        print(f"Total missing values before cleaning: {missing_before}")

        numeric_columns = self.cleaned_df.select_dtypes(
            include=[np.number]).columns
        for col in numeric_columns:
            if self.cleaned_df[col].isnull().any():
                self.cleaned_df[col].fillna(
                    self.cleaned_df[col].mean(), inplace=True)
                print(f"  • Filled {col} with mean value")

        if date_column in self.cleaned_df.columns:
            initial_rows = len(self.cleaned_df)
            self.cleaned_df.dropna(subset=[date_column], inplace=True)
            dropped = initial_rows - len(self.cleaned_df)
            if dropped > 0:
                print(f"  • Dropped {dropped} rows with missing dates")

        if date_column in self.cleaned_df.columns:
            print(f"\n--- Converting Date Column ---")
            try:
                self.cleaned_df[date_column] = pd.to_datetime(
                    self.cleaned_df[date_column])
                print(
                    f"✓ Successfully converted '{date_column}' to datetime format")
            except Exception as e:
                print(f"Warning: Could not convert date column: {e}")

        print(f"\n--- Available Columns ---")
        print(self.cleaned_df.columns.tolist())
        missing_after = self.cleaned_df.isnull().sum().sum()
        print(f"\nTotal missing values after cleaning: {missing_after}")
        print(f"✓ Cleaned dataset shape: {self.cleaned_df.shape}")
        return self.cleaned_df

    def compute_statistics(self, numeric_columns=None):
        print("\n" + "=" * 70)
        print("TASK 3: STATISTICAL ANALYSIS WITH NUMPY")
        print("=" * 70)

        if self.cleaned_df is None:
            print("Error: Data not cleaned. Run clean_and_process_data() first.")
            return

        if numeric_columns is None:
            numeric_columns = self.cleaned_df.select_dtypes(
                include=[np.number]).columns.tolist()

        print(f"\nAnalyzing columns: {numeric_columns}")
        stats_summary = {}

        for col in numeric_columns:
            if col in self.cleaned_df.columns:
                data = self.cleaned_df[col].dropna().values
                stats_summary[col] = {
                    'Mean': np.mean(data),
                    'Median': np.median(data),
                    'Std Dev': np.std(data),
                    'Min': np.min(data),
                    'Max': np.max(data),
                    'Range': np.max(data) - np.min(data),
                    'Q1': np.percentile(data, 25),
                    'Q3': np.percentile(data, 75)
                }

        print("\n--- Statistical Summary ---")
        for col, stats in stats_summary.items():
            print(f"\n{col}:")
            for stat_name, stat_value in stats.items():
                print(f"  {stat_name:12}: {stat_value:10.2f}")
        return stats_summary

    def create_visualizations(self, date_column='Date', temp_column=None,
                              rainfall_column=None, humidity_column=None):
        print("\n" + "=" * 70)
        print("TASK 4: VISUALIZATION WITH MATPLOTLIB")
        print("=" * 70)

        if self.cleaned_df is None:
            print("Error: Data not cleaned. Run clean_and_process_data() first.")
            return

        if date_column not in self.cleaned_df.columns:
            date_cols = [
                col for col in self.cleaned_df.columns if 'date' in col.lower()]
            date_column = date_cols[0] if date_cols else self.cleaned_df.columns[0]

        numeric_cols = self.cleaned_df.select_dtypes(
            include=[np.number]).columns.tolist()

        if temp_column is None and numeric_cols:
            temp_candidates = [
                col for col in numeric_cols if 'temp' in col.lower()]
            temp_column = temp_candidates[0] if temp_candidates else numeric_cols[0]

        if rainfall_column is None and len(numeric_cols) > 1:
            rain_candidates = [
                col for col in numeric_cols if 'rain' in col.lower()]
            rainfall_column = rain_candidates[0] if rain_candidates else numeric_cols[1]

        if humidity_column is None and len(numeric_cols) > 2:
            humidity_candidates = [
                col for col in numeric_cols if 'humidity' in col.lower() or 'humid' in col.lower()]
            humidity_column = humidity_candidates[0] if humidity_candidates else numeric_cols[2]

        print(f"\nUsing columns:")
        print(f"  Date: {date_column}")
        print(f"  Temperature: {temp_column}")
        print(f"  Rainfall: {rainfall_column}")
        print(f"  Humidity: {humidity_column}")

        plot_df = self.cleaned_df[[date_column]].copy()
        for col in [temp_column, rainfall_column, humidity_column]:
            if col and col in self.cleaned_df.columns:
                plot_df[col] = self.cleaned_df[col]
        plot_df.set_index(date_column, inplace=True)

        fig = plt.figure(figsize=(16, 12))

        if temp_column:
            ax1 = plt.subplot(2, 2, 1)
            ax1.plot(plot_df.index, plot_df[temp_column],
                     color='red', linewidth=1.5, alpha=0.8)
            ax1.fill_between(
                plot_df.index, plot_df[temp_column], alpha=0.3, color='red')
            ax1.set_title('Daily Temperature Trends',
                          fontsize=14, fontweight='bold')
            ax1.set_xlabel('Date')
            ax1.set_ylabel('Temperature (°C)')
            ax1.grid(True, alpha=0.3)
            plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)

        if rainfall_column:
            ax2 = plt.subplot(2, 2, 2)
            monthly_rainfall = plot_df[rainfall_column].resample('M').sum()
            ax2.bar(range(len(monthly_rainfall)),
                    monthly_rainfall.values, color='steelblue', alpha=0.8)
            ax2.set_title('Monthly Rainfall Totals',
                          fontsize=14, fontweight='bold')
            ax2.set_xlabel('Month')
            ax2.set_ylabel('Rainfall (mm)')
            ax2.set_xticks(range(len(monthly_rainfall)))
            ax2.set_xticklabels([date.strftime('%b')
                                for date in monthly_rainfall.index], rotation=45)
            ax2.grid(True, alpha=0.3, axis='y')

        if humidity_column and temp_column:
            ax3 = plt.subplot(2, 2, 3)
            ax3.scatter(
                plot_df[temp_column], plot_df[humidity_column], alpha=0.5, color='green', s=30)
            ax3.set_title('Humidity vs. Temperature',
                          fontsize=14, fontweight='bold')
            ax3.set_xlabel('Temperature (°C)')
            ax3.set_ylabel('Humidity (%)')
            ax3.grid(True, alpha=0.3)
            z = np.polyfit(plot_df[temp_column].dropna(),
                           plot_df[humidity_column].dropna(), 1)
            p = np.poly1d(z)
            x_trend = np.linspace(
                plot_df[temp_column].min(), plot_df[temp_column].max(), 100)
            ax3.plot(x_trend, p(x_trend), "r--",
                     alpha=0.8, linewidth=2, label='Trend')
            ax3.legend()

        if temp_column:
            ax4 = plt.subplot(2, 2, 4)
            monthly_temp = plot_df[temp_column].resample(
                'M').agg(['mean', 'min', 'max'])
            ax4.plot(monthly_temp.index, monthly_temp['mean'], marker='o',
                     color='darkred', linewidth=2, label='Mean', markersize=8)
            ax4.fill_between(
                monthly_temp.index, monthly_temp['min'], monthly_temp['max'], alpha=0.3, color='red', label='Min-Max Range')
            ax4.set_title('Monthly Temperature Statistics',
                          fontsize=14, fontweight='bold')
            ax4.set_xlabel('Month')
            ax4.set_ylabel('Temperature (°C)')
            ax4.legend()
            ax4.grid(True, alpha=0.3)
            plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45)

        plt.tight_layout()
        plot_path = self.output_dir / "weather_analysis_combined.png"
        plt.savefig(plot_path, dpi=300, bbox_inches='tight')
        print(f"\n✓ Saved combined plot: {plot_path}")
        plt.close()

        self._save_individual_plots(
            plot_df, temp_column, rainfall_column, humidity_column)

    def _save_individual_plots(self, plot_df, temp_column, rainfall_column, humidity_column):
        if temp_column:
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(plot_df.index,
                    plot_df[temp_column], color='red', linewidth=2)
            ax.fill_between(
                plot_df.index, plot_df[temp_column], alpha=0.3, color='red')
            ax.set_title('Daily Temperature Trends',
                         fontsize=14, fontweight='bold')
            ax.set_xlabel('Date')
            ax.set_ylabel('Temperature (°C)')
            ax.grid(True, alpha=0.3)
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
            plt.tight_layout()
            plt.savefig(self.output_dir / "01_temperature_trends.png",
                        dpi=300, bbox_inches='tight')
            print(f"✓ Saved: 01_temperature_trends.png")
            plt.close()

        if rainfall_column:
            fig, ax = plt.subplots(figsize=(12, 6))
            monthly_rainfall = plot_df[rainfall_column].resample('M').sum()
            ax.bar(range(len(monthly_rainfall)),
                   monthly_rainfall.values, color='steelblue', alpha=0.8)
            ax.set_title('Monthly Rainfall Totals',
                         fontsize=14, fontweight='bold')
            ax.set_xlabel('Month')
            ax.set_ylabel('Rainfall (mm)')
            ax.set_xticks(range(len(monthly_rainfall)))
            ax.set_xticklabels([date.strftime('%b %Y')
                               for date in monthly_rainfall.index], rotation=45)
            ax.grid(True, alpha=0.3, axis='y')
            plt.tight_layout()
            plt.savefig(self.output_dir / "02_monthly_rainfall.png",
                        dpi=300, bbox_inches='tight')
            print(f"✓ Saved: 02_monthly_rainfall.png")
            plt.close()

        if humidity_column and temp_column:
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.scatter(
                plot_df[temp_column], plot_df[humidity_column], alpha=0.5, color='green', s=40)
            ax.set_title('Humidity vs. Temperature',
                         fontsize=14, fontweight='bold')
            ax.set_xlabel('Temperature (°C)')
            ax.set_ylabel('Humidity (%)')
            ax.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig(self.output_dir / "03_humidity_vs_temperature.png",
                        dpi=300, bbox_inches='tight')
            print(f"✓ Saved: 03_humidity_vs_temperature.png")
            plt.close()

    def group_and_aggregate(self, date_column='Date', group_by='M'):
        print("\n" + "=" * 70)
        print("TASK 5: GROUPING AND AGGREGATION")
        print("=" * 70)

        if self.cleaned_df is None:
            print("Error: Data not cleaned. Run clean_and_process_data() first.")
            return

        if date_column in self.cleaned_df.columns:
            if not pd.api.types.is_datetime64_any_dtype(self.cleaned_df[date_column]):
                self.cleaned_df[date_column] = pd.to_datetime(
                    self.cleaned_df[date_column])

        numeric_cols = self.cleaned_df.select_dtypes(
            include=[np.number]).columns.tolist()
        temp_df = self.cleaned_df.set_index(date_column)

        freq_name = {'D': 'Daily', 'M': 'Monthly', 'Y': 'Yearly'}[group_by]
        print(f"\n--- {freq_name} Aggregated Statistics ---")

        aggregated = temp_df[numeric_cols].resample(
            group_by).agg(['mean', 'sum', 'min', 'max'])
        print(aggregated)

        agg_path = self.output_dir / f"aggregated_data_{group_by}.csv"
        aggregated.to_csv(agg_path)
        print(f"\n✓ Saved aggregated data: {agg_path}")
        return aggregated

    def export_cleaned_data(self, output_filename='cleaned_weather_data.csv'):
        print("\n" + "=" * 70)
        print("TASK 6: EXPORT AND REPORTING")
        print("=" * 70)

        if self.cleaned_df is None:
            print("Error: Data not cleaned. Run clean_and_process_data() first.")
            return

        output_path = self.output_dir / output_filename
        self.cleaned_df.to_csv(output_path, index=False)
        print(f"\n✓ Exported cleaned data to: {output_path}")
        print(
            f"  Dimensions: {self.cleaned_df.shape[0]} rows × {self.cleaned_df.shape[1]} columns")
        return output_path

    def generate_report(self, report_filename='WEATHER_ANALYSIS_REPORT.md'):
        if self.cleaned_df is None:
            print("Error: Data not cleaned. Run clean_and_process_data() first.")
            return

        report_path = self.output_dir / report_filename
        numeric_cols = self.cleaned_df.select_dtypes(
            include=[np.number]).columns.tolist()

        with open(report_path, 'w') as f:
            f.write("# Weather Data Analysis Report\n\n")
            f.write(
                f"**Generated:** {datetime.now().strftime('%B %d, %Y at %H:%M:%S')}\n\n")
            f.write("## Executive Summary\n\n")
            f.write(
                "This report presents a comprehensive analysis of weather data with statistical ")
            f.write("insights and visualizations.\n\n")
            f.write("## 1. Dataset Overview\n\n")
            f.write(f"- **Total Records:** {self.cleaned_df.shape[0]:,}\n")
            f.write(f"- **Total Features:** {self.cleaned_df.shape[1]}\n")
            f.write(
                f"- **Missing Values (post-cleaning):** {self.cleaned_df.isnull().sum().sum()}\n\n")
            f.write("## 2. Statistical Analysis\n\n")

            for col in numeric_cols:
                data = self.cleaned_df[col].dropna().values
                f.write(f"\n### {col}\n")
                f.write(f"- **Mean:** {np.mean(data):.2f}\n")
                f.write(f"- **Median:** {np.median(data):.2f}\n")
                f.write(f"- **Std Deviation:** {np.std(data):.2f}\n")
                f.write(f"- **Min:** {np.min(data):.2f}\n")
                f.write(f"- **Max:** {np.max(data):.2f}\n")
                f.write(f"- **Range:** {np.max(data) - np.min(data):.2f}\n")

            f.write("\n## 3. Visualizations\n\n")
            f.write(
                "Generated charts: Temperature trends, Monthly rainfall, Humidity vs temperature, Monthly statistics\n\n")
            f.write("## 4. Conclusion\n\n")
            f.write(
                "Analysis complete. Review visualizations and aggregated data for insights.\n\n")
            f.write("---\n")
            f.write(
                f"*Report generated automatically on {datetime.now().strftime('%B %d, %Y')}*\n")

        print(f"✓ Generated report: {report_path}")
        return report_path


def main():
    print("\n" + "=" * 70)
    print("WEATHER DATA VISUALIZER - MINI PROJECT")
    print("=" * 70 + "\n")

    csv_file = "weather_data.csv"

    if not os.path.exists(csv_file):
        print(f"ERROR: {csv_file} not found!")
        print("\nTo use this project:")
        print("1. Place weather CSV file in the same directory as this script")
        print("2. CSV should have columns: Date, Temperature, Rainfall, Humidity, Pressure")
        return

    visualizer = WeatherDataVisualizer(csv_file)

    try:
        visualizer.load_and_inspect_data()
        visualizer.clean_and_process_data()
        visualizer.compute_statistics()
        visualizer.create_visualizations()
        visualizer.group_and_aggregate()
        visualizer.export_cleaned_data()
        visualizer.generate_report()

        print("\n" + "=" * 70)
        print("✓ ALL TASKS COMPLETED SUCCESSFULLY!")
        print("=" * 70)
        print("\nOutput files saved to './output/' directory:")
        print("  • weather_analysis_combined.png")
        print("  • 01_temperature_trends.png")
        print("  • 02_monthly_rainfall.png")
        print("  • 03_humidity_vs_temperature.png")
        print("  • cleaned_weather_data.csv")
        print("  • aggregated_data_M.csv")
        print("  • WEATHER_ANALYSIS_REPORT.md\n")

    except Exception as e:
        print(f"\n✗ Error during execution: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
